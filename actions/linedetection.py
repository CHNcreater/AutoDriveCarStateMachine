import numpy as np
import cv2
import sys

def region_selection(image):
	"""
	Determine and cut the region of interest in the input image.
	Parameters:
		image: we pass here the output from canny where we have 
		identified edges in the frame
	"""
	# create an array of the same size as of the input image 
	mask = np.zeros_like(image) 
	# if you pass an image with more then one channel
	if len(image.shape) > 2:
		channel_count = image.shape[2]
		ignore_mask_color = (255,) * channel_count
	# our image only has one channel so it will go under "else"
	else:
		# color of the mask polygon (white)
		ignore_mask_color = 255
	# creating a polygon to focus only on the road in the picture
	# we have created this polygon in accordance to how the camera was placed
	height, width = image.shape
    # 定义感兴趣区域的多边形顶点
	polygon = np.array([[(0, height),(width, height),(width, height * 0.5),(0, height * 0.5)]], np.int32)
	# filling the polygon with white color and generating the final mask
	cv2.fillPoly(mask, polygon, ignore_mask_color)
	# performing Bitwise AND on the input image and mask to get only the edges on the road
	masked_image = cv2.bitwise_and(image, mask)
	return masked_image

def hough_transform(image):
	"""
	Determine and cut the region of interest in the input image.
	Parameter:
		image: grayscale image which should be an output from the edge detector
	"""
	# Distance resolution of the accumulator in pixels.
	rho = 1			
	# Angle resolution of the accumulator in radians.
	theta = np.pi/180
	# Only lines that are greater than threshold will be returned.
	threshold = 50
	# Line segments shorter than that are rejected.
	minLineLength = 50
	# Maximum allowed gap between points on the same line to link them
	maxLineGap = 100	
	# function returns an array containing dimensions of straight lines 
	# appearing in the input image
	return cv2.HoughLinesP(image, rho = rho, theta = theta, threshold = threshold,
						minLineLength = minLineLength, maxLineGap = maxLineGap)
	
def average_slope_intercept(lines):
	"""
	Find the slope and intercept of the left and right lanes of each image.
	Parameters:
		lines: output from Hough Transform
	"""
	left_lines = [] #(slope, intercept)
	left_weights = [] #(length,)
	right_lines = [] #(slope, intercept)
	right_weights = [] #(length,)
	
	for line in lines:
		for x1, y1, x2, y2 in line:
			if x1 == x2:
				continue
			# calculating slope of a line
			slope = (y2 - y1) / (x2 - x1)
			# calculating intercept of a line
			intercept = y1 - (slope * x1)
			# calculating length of a line
			length = np.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
			# slope of left lane is negative and for right lane slope is positive
			if slope < 0:
				left_lines.append((slope, intercept))
				left_weights.append((length))
			else:
				right_lines.append((slope, intercept))
				right_weights.append((length))
	# 
	left_lane = np.dot(left_weights, left_lines) / np.sum(left_weights) if len(left_weights) > 0 else None
	right_lane = np.dot(right_weights, right_lines) / np.sum(right_weights) if len(right_weights) > 0 else None
	return left_lane, right_lane

def pixel_points(y1, y2, line):
	"""
	Converts the slope and intercept of each line into pixel points.
		Parameters:
			y1: y-value of the line's starting point.
			y2: y-value of the line's end point.
			line: The slope and intercept of the line.
	"""
	if line is None:
		return None
	slope, intercept = line
	x1 = int((y1 - intercept)/slope)
	x2 = int((y2 - intercept)/slope)
	y1 = int(y1)
	y2 = int(y2)
	return ((x1, y1), (x2, y2))

def lane_lines(image, lines):
	"""
	Create full lenght lines from pixel points.
		Parameters:
			image: The input test image.
			lines: The output lines from Hough Transform.
	"""
	left_lane, right_lane = average_slope_intercept(lines)
	y1 = image.shape[0]
	y2 = y1 * 0.5
	left_line = pixel_points(y1, y2, left_lane)
	right_line = pixel_points(y1, y2, right_lane)
	center_line = (((left_line[0][0] + right_line[0][0]) // 2, (left_line[0][1] + right_line[0][1]) // 2), ((left_line[1][0] + right_line[1][0]) // 2, (left_line[1][1] + right_line[1][1]) // 2))
	return left_line, right_line, center_line
	
def draw_lane_lines(image, lines, color=[255, 0, 0], thickness=12):
	"""
	Draw lines onto the input image.
		Parameters:
			image: The input test image (video frame in our case).
			lines: The output lines from Hough Transform.
			color (Default = red): Line color.
			thickness (Default = 12): Line thickness. 
	"""
	line_image = np.zeros_like(image)
	for line in lines:
		if line is not None:
			cv2.line(line_image, *line, color, thickness)
	return cv2.addWeighted(image, 1.0, line_image, 1.0, 0.0)

def calculate_steering_angle(frame, lines):
    height, width, _ = frame.shape
    _, _, center_line = lane_lines(frame, lines)
    x1, y1 = center_line[0]
    x2, y2 = center_line[1]
	# calculating slope of a line
    slope = (y2 - y1) / (x2 - x1)
	# calculating intercept of a line
    intercept = y1 - (slope * x1)
    mid_y = slope * (width / 2) + intercept
    # 计算车道中心线
    mid_x = x1
	# 计算转向角度
    steering_angle = np.arctan2(height - mid_y, width / 2 - mid_x) * 180 / np.pi
    if abs(steering_angle - 90 < 5):
        return 0
    else:
        if slope < 0:
            return abs(steering_angle - 90)
        else:
            return -1 * abs(steering_angle - 90)

def detect_and_handle_corner(steering_angle, previous_angle):
    # 如果转向角度变化较大，可能是遇到了直角弯
    if abs(steering_angle - previous_angle) > 30:
        # 调整转向角度以应对直角弯
        if steering_angle > previous_angle:
            steering_angle = previous_angle + 90
        else:
            steering_angle = previous_angle - 90
    return steering_angle

def frame_processor_test(image):
	"""
	Process the input frame to detect lane lines.
	Parameters:
		image: image of a road where one wants to detect lane lines
		(we will be passing frames of video to this function)
	"""
	# convert the RGB image to Gray scale
	grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# applying gaussian Blur which removes noise from the image 
	# and focuses on our region of interest
	# size of gaussian kernel
	kernel_size = 5
	# Applying gaussian blur to remove noise from the frames
	blur = cv2.GaussianBlur(grayscale, (kernel_size, kernel_size), 0)
	# first threshold for the hysteresis procedure
	low_t = 200
	# second threshold for the hysteresis procedure 
	high_t = 255
	# applying canny edge detection and save edges in a variable
	edges = cv2.Canny(blur, low_t, high_t)
	# since we are getting too many edges from our image, we apply 
	# a mask polygon to only focus on the road
	# Will explain Region selection in detail in further steps
	region = region_selection(edges)
	# Applying hough transform to get straight lines from our image 
	# and find the lane lines
	# Will explain Hough Transform in detail in further steps
	hough = hough_transform(region)
	steering_angle = calculate_steering_angle(image, hough)
	print("Steering Angle: ", steering_angle)
	#lastly we draw the lines on our resulting frame and return it as output 
	result = draw_lane_lines(image, lane_lines(image, hough))
	return result

def line_detection(image):
    """
    return turning angle, if positve, turn right, else turn left by a specific angle
    """
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5, 5), 0)
    edges = cv2.Canny(blur, 200, 255)
    region = region_selection(edges)
    hough = hough_transform(region)
    return calculate_steering_angle(image, hough)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python linedetection.py <image_path>")
		sys.exit(1)

	image_path = f'../data/lines/{sys.argv[1]}.jpg' # path to the image
	image = cv2.imread(image_path)
	if image is not None:
		processed_image = frame_processor_test(image)
		cv2.imshow('Processed Image', processed_image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		print("Error: Unable to read the image.")