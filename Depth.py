import pyzed.sl as sl
import numpy as np
import cv2, time

def main():
     # Create a Camera object
    zed = sl.Camera()
    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_MEDIUM
    init_params.coordinate_units = sl.UNIT.UNIT_METER
    #init_params.depth_minimum_distance = 0.3

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Error opening camera")
        print(err)
        exit(1)

    runtime_parameters =sl.RuntimeParameters()
    runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_FILL
    
    rows = 720
    cols = 1280
    M = np.float32([[1,0,300],[0,1,0]])
    M2 = np.float32([[1,0,-300],[0,1,0]])
    #Capture an ideal image
    depth_image = sl.Mat()
    zed.retrieve_image(depth_image, sl.VIEW.VIEW_DEPTH)
    idealDepthImage = cv2.resize(depth_image.get_data(), (0,0), fx=0.5, fy=0.5)

    try:
        while True:
            depth_image = sl.Mat()
            depth_map  = sl.Mat()
            rgb_left_image = sl.Mat()
            rgb_image = sl.Mat()
            if zed.grab(runtime_parameters) ==  sl.ERROR_CODE.SUCCESS :
                zed.retrieve_image(depth_image, sl.VIEW.VIEW_DEPTH)
                zed.retrieve_image(rgb_image, sl.VIEW.VIEW_LEFT)
                zed.retrieve_measure(depth_map, sl.MEASURE.MEASURE_DEPTH)

                hsv_rgb = cv2.cvtColor(rgb_image.get_data(), cv2.COLOR_BGR2HSV)
                hsv_rgb = cv2.resize(hsv_rgb, (0,0), fx=0.5, fy=0.5)
                gray_rgb = cv2.cvtColor(rgb_image.get_data(), cv2.COLOR_BGR2GRAY)

                gray_rgb = cv2.resize(gray_rgb, (0,0), fx=0.5, fy=0.5)
                hsvmean = cv2.mean(hsv_rgb)[2]
                resizedDepthImage = cv2.resize(depth_image.get_data(), (0,0), fx=0.5, fy=0.5)
                
                #Compare to ideal image
                sub = idealDepthImage - resizedDepthImage
                sub = abs(sub)
                threshold = 200
                sub[sub >= threshold] = 255
                sub[sub < threshold] = 0

                mean = cv2.mean(resizedDepthImage)[0]
                min_threshold = 15
                max_threshold = 50

                edges = cv2.Canny(resizedDepthImage,min_threshold,max_threshold)
                rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
                rgb *= np.array((0,0,1),np.uint8)
                depthImageConvertedToColor = cv2.cvtColor(resizedDepthImage, cv2.COLOR_BGRA2BGR)
                out = np.bitwise_or(depthImageConvertedToColor, rgb)

                cv2.imshow('Zed2', depth_image.get_data())
                cv2.waitKey(1)
                



    except Exception as e:
        print(e)
        zed.close()
        exit(1)


if __name__ == "__main__":
    print("Start")
    main()
