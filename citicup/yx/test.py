import GarbageClassification as GC

if __name__ == '__main__':
    img_path = "./test_img/glass103.jpg"
    pred = GC.predict_img(img_path)
    print(pred)