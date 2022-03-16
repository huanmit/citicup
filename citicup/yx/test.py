import GarbageClassification as GC

if __name__ == '__main__':
    img_path = "test_img/img4GC/trash1.jpg"
    pred = GC.predict_img(img_path)
    print(pred)