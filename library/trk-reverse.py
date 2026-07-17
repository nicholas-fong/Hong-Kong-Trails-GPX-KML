import os
import xml.etree.ElementTree as ET

def reverse_gpx_track(input_path, output_path, strip_time=True):
    # Register the standard GPX namespace to keep the output file clean
    ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
    
    # Parse the GPX file
    tree = ET.parse(input_path)
    root = tree.getroot()
    
    # Find all track segments (handles namespaces dynamically)
    for trkseg in root.iter():
        if trkseg.tag.endswith('trkseg'):
            # Extract all track points in this segment
            points = [child for child in trkseg if child.tag.endswith('trkpt')]
            
            # Remove the original points from the segment
            for pt in points:
                trkseg.remove(pt)
            
            # Strip timestamps if requested
            if strip_time:
                for pt in points:
                    time_elements = [child for child in pt if child.tag.endswith('time')]
                    for t in time_elements:
                        pt.remove(t)
            
            # Re-append the points in reverse order
            for pt in reversed(points):
                trkseg.append(pt)
                
    # Save the modified GPX data to a new file
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"Done! Reversed track saved to: {output_path}")

if __name__ == "__main__":
    # 1. Ask user for input and output filenames
    input_file = input("Enter the input GPX filename: ").strip()
    output_file = input("Enter the output GPX filename: ").strip()
    
    # 2. Check if the input file actually exists
    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' does not exist.")
    # 3. Warning: If output file exists, issue a warning and stop
    elif os.path.exists(output_file):
        print(f"Warning: The output file '{output_file}' already exists. Operation aborted to prevent overwriting.")
    else:
        # 4. Run the function if everything is safe
        try:
            reverse_gpx_track(input_file, output_file)
        except Exception as e:
            print(f"An error occurred while processing the GPX file: {e}")