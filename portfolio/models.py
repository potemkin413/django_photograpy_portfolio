from django.db import models


class side_bar(models.Model):
    """Меню сайта"""
    title = models.TextField("Заголовок", default="Example title", max_length=100)
    main = models.CharField("Название кнопки 'Главная'", default="Main", max_length=20)
    services = models.CharField("Название кнопки 'Услуги'", default="Services", max_length=20)
    portfolio = models.CharField("Название кнопки 'Портфолио'", default="Portfolio", max_length=20)
    clients = models.CharField("Название кнопки 'Клиенты'", default="Clients", max_length=20)
    about_me = models.CharField("Название кнопки 'Обо мне'", default="About me", max_length=20)
    contacts = models.CharField("Название кнопки 'Связь со мной'", default="Contacts", max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sidebar"
        verbose_name_plural = "Sidebar"


class intro(models.Model):
    """Интро на сайте"""
    slogan = models.TextField("Слоган", default="Example slogan")
    motto = models.TextField("Девиз", default="Example motto")
    image = models.ImageField("Фотография интро")
    description = models.TextField("Информация о себе", default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", max_length=5000)

    def __str__(self):
        return self.slogan

    class Meta:
        verbose_name = "Intro"
        verbose_name_plural = "Intro"


class services(models.Model):
    """Блок услуги"""
    title = models.CharField("Заголовок блока", default="servisec", max_length=50)
    slogan = models.TextField("Слоган", default="Example slogan", max_length=300)
    name_service_first = models.CharField("Название первой услуги", max_length=50, default='First service')
    description_service_first = models.TextField("Описание первой услуги", max_length=300,
                                                 default="Description first service")
    image_service_first = models.ImageField("Картинка первой услуги")

    name_service_second = models.CharField("Название второй услуги", max_length=50, default='First service')
    description_service_second = models.TextField("Описание второй услуги", max_length=300,
                                                 default="Description first service")
    image_service_second = models.ImageField("Картинка второй услуги")

    name_service_third = models.CharField("Название третьей услуги", max_length=50, default='First service')
    description_service_third = models.TextField("Описание третьей услуги", max_length=300,
                                                 default="Description first service")
    image_service_third = models.ImageField("Картинка третьей услуги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class portfolio(models.Model):
    """Фотографии в портфолио"""
    title = models.CharField("Заголовок блока", default="title", max_length=50)
    name = models.CharField("Название фотографии в базе данных",max_length=50)
    image = models.ImageField("Фотография в портфолио", default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class clients(models.Model):
    """Фотографии логотипов клиентов"""
    name = models.CharField("Название клиента в базе данных", max_length=50)
    image = models.ImageField("Фотография логотипа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class about_me(models.Model):
    """Информация обо мне"""
    title = models.CharField("Заголовок блока", default="Example title ABOUT ME", max_length=100)
    slogan = models.CharField("Ваш слоган", default='Lorem slogan', max_length=200)
    description = models.TextField("Подробная информация о ВАС", default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    image = models.ImageField("Фотография в блоке")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"


class contact_me(models.Model):
    """Контакты для связи"""
    title = models.CharField("Название блока", default="Contact me", max_length=100)
    slogan = models.CharField("Ваш слоган", default="Example slogan", max_length=150)
    email = models.EmailField("Ваша электронная почта")
    place = models.CharField("Ваше месторасположение", default="Example", max_length=100)
    description = models.TextField("Описание", default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact me"
        verbose_name_plural = "Contact me"


class footer(models.Model):
    text = models.CharField("Текст футора", default="©Developed by Potemkin Nikita", max_length=1000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"





