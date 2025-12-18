# Handle multiple Exception

list_all = ['a',123, 456, 'qwerty'] # mixed list of integer and string

try:
    total = list_all[1] + list_all[2] # we can add list_add[3], it will goto except part
    print(f"Value Added, {total}")
except (ValueError, TypeError) as e:
    print(f"Total value isn't added because of incorrect data")
except:
    print("Out of range")
finally:
    print("Thanks")