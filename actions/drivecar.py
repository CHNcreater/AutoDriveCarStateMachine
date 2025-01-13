from objectdetectiontextrecognition import ObjectDetectionTextRecognition

def drive_car():
    """drive the car
    """
    res = ObjectDetectionTextRecognition.main()
    if res == "stop":
        return False
    else :
        return True