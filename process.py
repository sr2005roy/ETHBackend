import face_recognition

def is_face_match(image_path_1, image_path_2):
    # Load the first image and encode the face
    picture_of_me = face_recognition.load_image_file(image_path_1)
    my_face_encodings = face_recognition.face_encodings(picture_of_me)

    if len(my_face_encodings) == 0:
        raise ValueError(f"No face found in image {image_path_1}")
    my_face_encoding = my_face_encodings[0]

    # Load the second image and encode the face
    unknown_picture = face_recognition.load_image_file(image_path_2)
    unknown_face_encodings = face_recognition.face_encodings(unknown_picture)

    if len(unknown_face_encodings) == 0:
        raise ValueError(f"No face found in image {image_path_2}")
    unknown_face_encoding = unknown_face_encodings[0]

    # Compare faces and convert numpy.bool_ to Python bool
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    # Return True if it's a match, False otherwise
    return bool(results[0])  # Convert to native Python bool
