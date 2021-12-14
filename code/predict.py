import tensorflow as tf
import numpy as np
from models import VGGModel
import hyperparameters as hp

def predict_image(path):
    model = VGGModel
    data_dir = "\Users\katie\Documents\Classes\cs1430\inside-out\data"
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=hp.img_size,
        batch_size=hp.batch_size)

    class_names = train_ds.class_names

    url = path
    path = tf.keras.utils.get_file(fname="~happy~", origin=url)

    img = tf.keras.utils.load_img(path)

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print("This image msot loikely belongs to {} with a {:.2f} percent confidence."
          .format(class_names[np.argmax(score)], 100 * np.max(score)))
