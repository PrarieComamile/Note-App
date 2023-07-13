# Note-App

Note App, kullanıcıların notlarını kolaylıkla kaydedebilecekleri ve organize edebilecekleri bir web uygulamasıdır.

# **Kurulum**

**1. Gereksinimlerin Kurulumu**
- Python 3.10 veya daha yeni bir sürümün yüklü olduğundan emin olun.
- Projeyi çalıştırmak için aşağıdaki komutu kullanarak Flask ve diğer bağımlılıkları yükleyin:

      pip install -r requirements.txt

**2. Veritabanı Yapılandırması**

**Database Oluşturma:**

    CREATE DATABASE noteapp;


**Tablo Oluşturma:**

    USE noteapp;
    CREATE TABLE users (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name TEXT,      
        email TEXT,
        username TEXT,
        password TEXT
    );

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


# Site Görüntüleri

![Screenshot from 2023-07-13 16-07-15](https://github.com/PrarieComamile/Note-App/assets/101043132/e1b636b2-cb73-47e0-888e-9b785bd2f3f3)
![Screenshot from 2023-07-13 16-07-24](https://github.com/PrarieComamile/Note-App/assets/101043132/bdaca5f8-6065-449b-997e-5c94be44abd0)
![Screenshot from 2023-07-13 16-07-47](https://github.com/PrarieComamile/Note-App/assets/101043132/4eaf639c-c743-42f8-8c81-ac543ae2f9e0)


# Lisans 
  Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](https://github.com/PrarieComamile/Note-App/blob/main/LICENSE) dosyasını inceleyebilirsiniz.



