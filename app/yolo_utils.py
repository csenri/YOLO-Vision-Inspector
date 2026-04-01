import cv2
import numpy as np



def get_color(class_id):
    COLORS = [
    (255, 0, 0),   # Class 0: Blue
    (0, 255, 0),   # Class 1: Green
    (0, 0, 255),   # Class 2: Red
    (255, 255, 0), # Class 3: Cyan
    (255, 0, 255), # Class 4: Magenta
    (0, 255, 255), # Class 5: Yellow
    ]
    return COLORS[int(class_id) % len(COLORS)]

def yolo_box(path_image, path_annotation):
    img = cv2.imread(path_image, -1)
    out = img.copy()
    height, width, channels = img.shape
    annotation = open(path_annotation, 'r', encoding='utf-8')
    for line in annotation:
        data = np.array(line.strip().split()).astype(float)
        
        #<class_id> <x_center> <y_center> <w_norm> <h_norm>
        class_id = int(data[0])
        color = get_color(class_id)
        x_c, y_c, w_n, h_n = data[1], data[2], data[3], data[4]
        
        # Calculate bounding box coordinates
        tl_x = int((x_c - w_n / 2) * width)
        tl_y = int((y_c - h_n / 2) * height)
        br_x = int((x_c + w_n / 2) * width)
        br_y = int((y_c + h_n / 2) * height)
        
        # Draw the rectangle
        cv2.rectangle(out, (tl_x, tl_y), (br_x, br_y), color, 3)
        
        # Add class number text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(out, str(class_id), (tl_x, tl_y - 10), font, 1, color, 2, cv2.LINE_AA)
        
    return out

def yolo_seg(path_img, path_annotation):
    img = cv2.imread(path_img,-1)
    out = img.copy()
    height, width, channels = img.shape
    with open(path_annotation, 'r', encoding='utf-8') as annotation:
        for line in annotation:
            data = np.array(line.strip().split()).astype(float)
            # <class-index> <x1> <y1> <x2> <y2> ... <xn> <yn>
            class_id = int(data[0])
            color = get_color(class_id)
            normalized_points = data[1:].reshape(-1, 2)
            normalized_points[:, 0] *= width
            normalized_points[:, 1] *= height
            cv_points = normalized_points.astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(out, [cv_points], isClosed=True, color=color, thickness=2)

    return out


