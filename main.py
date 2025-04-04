import cv2
import time
from mano import Mano

def main():
    cap = cv2.VideoCapture(0)
    detector = Mano()

    ptiempo = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = detector.encontrar_manos(frame)

        ctiempo = time.time()
        fps = 1 / (ctiempo - ptiempo + 1e-6)  # evita division por cero
        ptiempo = ctiempo

        cv2.putText(frame, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Manos", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # esc para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
