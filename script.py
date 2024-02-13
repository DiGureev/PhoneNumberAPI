import phonenumbers

from phonenumbers import geocoder, carrier, timezone

def main(phone_number):

    #phone number
    parse = phonenumbers.parse(phone_number)
    national_number = parse.national_number

    valid_number = phonenumbers.is_valid_number(parse)

    #region of the number
    region = geocoder.description_for_number(parse, 'en')
    #number timezone
    phone_timezone = timezone.time_zones_for_number(parse)

    #Internet Service provider
    varrier = carrier.name_for_number(parse, 'en')

    data = {
        "phoneNumber": phone_number,
        "nationalNumber": national_number,
        "valid": valid_number,
        "region": region,
        "timezone": phone_timezone,
        "provider": varrier
    }
    return data


    