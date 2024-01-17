from shop.models import ProductImage  # Импортируйте вашу модель


def update_image_paths():
    images = ProductImage.objects.all()

    for image in images:
        old_path = str(image.image)
        # Предполагается, что новый путь - это старый путь без дополнительного 'shop/images/'
        new_path = old_path.replace('shop/images/shop/images/', 'shop/images/')

        # Обновляем путь, если он изменился
        if old_path != new_path:
            image.image = new_path
            image.save()
            print(f"Обновлен путь изображения: {old_path} -> {new_path}")


def delete_orphaned_images():
    images = ProductImage.objects.all()

    for image in images:
        if not image.image.storage.exists(image.image.name):
            print(f"Удаление несуществующего изображения: {image.image.name}")
            image.delete()


