
import sys
import cv2
from ultralytics import YOLO
from src.aglomeracao.logica_detector import verificar_aglomeracao

def main(video_path):
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)

    frame_id = 0
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)[0]
        pessoas = [det for det in results.boxes.data.tolist() if int(det[5]) == 0]  # classe 0 = pessoa

        if verificar_aglomeracao(len(pessoas), frame_id):
            print(f"Frame {frame_id}: Aglomeração detectada! Pessoas: {len(pessoas)}")

        frame_id += 1

    cap.release()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_video>")
    else:
        main(sys.argv[1])
