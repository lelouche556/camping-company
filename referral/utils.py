import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance):
    slug = "{randstr}".format(
                randstr=random_string_generator(size=6)
            )
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists > 0:
        unique_slug_generator(instance)

    return slug

