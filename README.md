# YOLO Vision Inspector 🔍


A web-based tool built with **FastAPI** and **OpenCV** to visualize YOLO (You Only Look Once) annotations directly in your browser. It supports both standard **Bounding Boxes** (object detection) and **Instance Segmentation** masks.

---

## ✨ Key Features

* **FastAPI Backend**
* **Web Interface**
* **Dual Visualization Modes**: Switch between Bounding Box and Instance Segmentation.
* **Dockerized**: Fully containerized environment for consistent deployment across any OS.

---
### Bounding Box Mode
* **Format**: `<class_id> <x_center> <y_center> <width> <height>` (normalized).

### Instance Segmentation Mode
* **Format**: `<class_id> <x1> <y1> <x2> <y2> ... <xn> <yn>` (normalized).

---

## 🚀 Getting Started

The easiest way to run the **YOLO Vision Inspector** is using Docker. This ensures that all dependencies (like OpenCV and system libraries) are configured correctly without polluting your local environment.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.
* [Git](https://git-scm.com/) installed.

### Installation & Deployment

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/csenri/YOLO-Vision-Inspector.git](https://github.com/csenri/YOLO-Vision-Inspector.git)
    cd YOLO-Vision-Inspector
    ```

2.  **Build the Docker Image**
    This command downloads the base Python image, installs system dependencies (`libgl1`, `libglib2.0-0`), and sets up the Python environment.
    ```bash
    docker build -t yolo-inspector .
    ```

3.  **Run the Container**
    Map port `8000` of your host computer to port `8000` of the container.
    ```bash
    docker run -p 8000:8000 yolo-inspector
    ```

4.  **Access the Application**
    Open your web browser and navigate to:
    👉 **[http://localhost:8000](http://localhost:8000)**

---
