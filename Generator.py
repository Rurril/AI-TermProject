class CaptchaGenerator(object):
      
  def __init__(self, image_length):
    self.image_length = image_length
    self.image_captcha = ImageCaptcha()

  def get_random_text(self):
    retVal = ''
    for _ in range(self.image_length):
        retVal += CHARSETS[random.randint(0, len(CHARSETS)-1)]
    return retVal

  def get_labeled_image(self, samples):
    X, Y = [], []
    for _ in range(samples):
        text = self.get_random_text()
        image = self.image_captcha.generate(text, format='png')
        captcha_image = Image.open(image)
        array = np.array(captcha_image)
        X.append(array)
        Y.append(text)
        self.image_captcha.write(text, "/content/drive/My Drive/AI/generated_captcha_images/%s.png" % text)
    return X, Y

def __main__():
    gen = CaptchaGenerator(4)
    gen.get_labeled_image(10000)