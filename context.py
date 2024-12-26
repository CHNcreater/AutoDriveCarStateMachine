import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('conf/config.ini')

# Example of accessing a configuration value
# Assuming the config file has a section 'Settings' with a key 'example_key'
example_value = config.get('mqtt', 'host')

print(f'Example value: {example_value}')