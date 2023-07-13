# Note-App

Note App, kullanıcıların notlarını kolaylıkla kaydedebilecekleri ve organize edebilecekleri bir web uygulamasıdır.

# **Kurulum**

**1. Gereksinimlerin Kurulumu**
- Python 3.10 veya daha yeni bir sürümün yüklü olduğundan emin olun.
- Projeyi çalıştırmak için aşağıdaki komutu kullanarak Flask ve diğer bağımlılıkları yükleyin:

      pip install -r requirements.txt

**2. Veritabanı Yapılandırması**
- MySQL veritabanı kurulumunu tamamlayın ve gerekli bağlantı bilgilerini `config.py` dosyasında tanımlayın.


**3. Uygulamanın Başlatması**
- Terminalde projenin ana dizinine gidin ve aşağıdaki komutu kullanarak Flask sunucusunu başlatın:

      flask run

- Tarayıcınızda `http://localhost:5000` adresine giderek uygulamayı görüntüleyebilirsiniz.




# Kullanılan Teknolojiler

- **Python**: Web uygulamasının arkasındaki programlama dili.

- **Flask**: Python tabanlı bir web framework'ü. Web uygulaması çatısı ve veritabanı yönetimi için kullanılmıştır.

- **Flask-MySQLdb**: Flask ile MySQL veritabanı arasındaki bağlantıyı sağlayan bir eklenti.

- **WTForms**: Formları oluşturmak ve doğrulamak için kullanılan bir kütüphane.

- **Passlib**: Parola hashleme ve doğrulama için kullanılan bir kütüphane.

# Lisans 
  Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](https://github.com/PrarieComamile/Note-App/blob/main/LICENSE) dosyasını inceleyebilirsiniz.




