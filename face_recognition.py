import cv2
import face_recognition

image = face_recognition.load_image_file("5.png")
person = "Furkan"
unknown_encoding = face_recognition.face_encodings(image)[0]
camera = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = camera.read()
    faceloc = face_recognition.face_locations(img)
    encoding2 = face_recognition.face_encodings(img, faceloc)

    if encoding2:
        matchedfaces = face_recognition.compare_faces(unknown_encoding, encoding2)
        a = 0

        for i in matchedfaces:
            if i:
                y, x2, y2, x = faceloc[a]
                cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)
                cv2.putText(img, person, (x, y - 10), font, 2, (255, 0, 255), 2)
            else:
                y, x2, y2, x = faceloc[a]
                cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, "Undefined", (x, y - 10), font, 2, (0, 200, 255), 2)
            a = a + 1

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
