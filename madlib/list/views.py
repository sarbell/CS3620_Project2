from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Lib, BrickElement, SeptemberElement, RockElement, CookieElement
from .forms import BrickForm, SeptemberForm, RockForm, CookieForm
from django import template


# Create your views here.

def home(request):
    mad_lib_list = Lib.objects.all()
    return render(request, 'list/home.html', {'mad_lib_list':mad_lib_list})


def brick_form(request):
    lib = Lib.objects.all()
    form = BrickForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list:brick_results')

    # nouns = []
    # plural_nouns = []
    # body_parts = []
    # accessories = []
    # clothing_items = []
    # locations = []
    # feelings = []
    # car_names = []
    # spices = []
    # time_days = []
    # measurements = []
    # temperatures = []
    # exclamations = []
    # unit_times = []
    # nicknames = []
    # numbers = []
    # large_numbers = []
    # famous_peoples = []
    # adjectives = []
    # adverbs = []
    # verbs = []
    # verbs_ing = []
    #
    # searching = True
    # while(searching):
    #     if lib.noun != 0:
    #         for i in range(0, lib.noun):
    #             nouns.append("Noun")
    #
    #     if lib.plural_noun !=0:
    #         for i in range(0, lib.plural_noun):
    #             plural_nouns.append("Plural Noun")
    #
    #     if lib.body_part !=0:
    #         for i in range(0, lib.body_part):
    #             body_parts.append("Body Part")
    #
    #     if lib.accessory !=0:
    #         for i in range(0, lib.accessory):
    #             accessories.append("Accessory")
    #
    #     if lib.clothing_item !=0:
    #         for i in range(0, lib.clothing_item):
    #             clothing_items.append("Clothing Item")
    #
    #     if lib.location !=0:
    #         for i in range(0, lib.location):
    #             locations.append("Location")
    #
    #     if lib.feeling !=0:
    #         for i in range(0, lib.feeling):
    #             feelings.append("Feeling")
    #
    #     if lib.car_name_or_type !=0:
    #         for i in range(0, lib.car_name_or_type):
    #             car_names.append("Car Name or Type")
    #
    #     if lib.spice !=0:
    #         for i in range(0, lib.spice):
    #             spices.append("Spice")
    #
    #     if lib.time_of_day != 0:
    #         for i in range(0, lib.time_of_day):
    #             time_days.append("Time of Day")
    #
    #     if lib.unit_of_measurement != 0:
    #         for i in range(0, lib.unit_of_measurement):
    #             measurements.append("Unit of Measurement")
    #
    #     if lib.temperature != 0:
    #         for i in range(0, lib.temperature):
    #             temperatures.append("Temperature")
    #
    #     if lib.exclamation !=0:
    #         for i in range(0, lib.exclamation):
    #             exclamations.append("Exclamation")
    #
    #     if lib.unit_of_time !=0:
    #         for i in range(0, lib.unit_of_time):
    #             unit_times.append("Unit of Time")
    #
    #     if lib.nickname !=0:
    #         for i in range(0, lib.nickname):
    #             nicknames.append("Nickname")
    #
    #     if lib.number !=0:
    #         for i in range(0, lib.number):
    #             numbers.append("Number")
    #
    #     if lib.large_number !=0:
    #         for i in range(0, lib.large_number):
    #             large_numbers.append("Large Number")
    #
    #     if lib.name_of_famous_person !=0:
    #         for i in range(0, lib.name_of_famous_person):
    #             famous_peoples.append("Name of Famous Person")
    #
    #     if lib.adjective !=0:
    #         for i in range(0, lib.adjective):
    #             adjectives.append("Adjective")
    #
    #     if lib.adverb !=0:
    #         for i in range(0, lib.adverb):
    #             adverbs.append("Adverb")
    #
    #     if lib.verb !=0:
    #         for i in range(0, lib.verb):
    #             verbs.append("Verb")
    #
    #     if lib.verb_ending_in_ing !=0:
    #         for i in range(0, lib.verb_ending_in_ing):
    #             verbs_ing.append("Verb Ending in 'ing'")
    #
    #     searching = False
    #
    #     lib_type_list = [
    #         nouns, plural_nouns, body_parts, accessories, clothing_items, locations, feelings, car_names,
    #         spices, time_days, measurements, temperatures, exclamations, unit_times, nicknames, numbers,
    #         large_numbers, famous_peoples, adjectives, adverbs, verbs, verbs_ing
    #     ]

    return render(request, 'list/brick-form.html', {'lib':lib, 'form':form})

def brick_result(request):
    results = BrickElement.objects.all().last()
    return render(request, 'list/brick-result.html', {'results': results})



def september_form(request):
    lib = Lib.objects.all()
    form = SeptemberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list:september_results')
    return render(request, 'list/september-form.html', {'lib':lib, 'form':form})

def september_result(request):
    results = SeptemberElement.objects.all().last()
    return render(request, 'list/september-result.html', {'results': results})


def rock_form(request):
    lib = Lib.objects.all()
    form = RockForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list:rock_results')
    return render(request, 'list/rock_form.html', {'lib':lib, 'form':form})


def rock_result(request):
    results = RockElement.objects.all().last()
    return render(request, 'list/rock_result.html', {'results': results})


def cookies_form(request):
    lib = Lib.objects.all()
    form = CookieForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list:cookies_results')
    return render(request, 'list/cookies-form.html', {'lib':lib, 'form':form})


def cookies_result(request):
    results = CookieElement.objects.all().last()
    return render(request, 'list/cookies-result.html', {'results': results})







# def show(request, id):
#     result = BrickElement.objects.all()
#     lib = Lib.objects.get(pk=id)
#     story = lib.text
#     mad_lib_words = story.split(" ")
#
#     nouns = []
#     plural_nouns = []
#     body_parts = []
#     accessories = []
#     clothing_items = []
#     locations = []
#     feelings = []
#     car_names = []
#     spices = []
#     time_days = []
#     measurements = []
#     temperatures = []
#     exclamations = []
#     unit_times = []
#     nicknames = []
#     numbers = []
#     large_numbers = []
#     famous_peoples = []
#     adjectives = []
#     adverbs = []
#     verbs = []
#     verbs_ing = []
#
#     for word in mad_lib_words:
#         if word == '[NOUN]':
#             for i in range(len(nouns)):
#                 story = story.replace("[NOUN]", nouns[i], 1)
#
#         if word == '[PLURAL_NOUN]':
#             for i in range(len(plural_nouns)):
#                 story = story.replace("[PLURAL_NOUN]", plural_nouns[i], 1)
#
#         if word == '[BODY_PARTS]':
#             for i in range(len(body_parts)):
#                 story = story.replace("[BODY_PART]", body_parts[i], 1)
#
#         if word == '[ACCESSORY]':
#             for i in range(len(accessories)):
#                 story = story.replace("[ACCESSORY]", accessories[i], 1)
#
#         if word == '[CLOTHING_ITEM]':
#             for i in range(len(clothing_items)):
#                 story = story.replace("[CLOTHING_ITEM]", clothing_items[i], 1)
#
#         if word == '[LOCATION]':
#             for i in range(len(locations)):
#                 story = story.replace("[LOCATION]", locations[i], 1)
#
#         if word == '[ACCESSORY]':
#             for i in range(len(accessories)):
#                 story = story.replace("[ACCESSORY]", accessories[i], 1)
#
#         if word == '[FEELING]':
#             for i in range(len(feelings)):
#                 story = story.replace("[FEELING]", feelings[i], 1)
#
#         if word == '[CAR_NAME_OR_TYPE]':
#             for i in range(len(car_names)):
#                 story = story.replace("[CAR_NAME_OR_TYPE]", car_names[i], 1)
#
#         if word == '[SPICE]':
#             for i in range(len(spices)):
#                 story = story.replace("[SPICE]", spices[i], 1)
#
#         if word == '[TIME_OF_DAY]':
#             for i in range(len(time_days)):
#                 story = story.replace("[TIME_OF_DAY]", time_days[i], 1)
#
#         if word == '[UNIT_OF_MEASUREMENT]':
#             for i in range(len(measurements)):
#                 story = story.replace("[UNIT_OF_MEASUREMENT]", measurements[i], 1)
#
#         if word == '[TEMPERATURE]':
#             for i in range(len(temperatures)):
#                 story = story.replace("[TEMPERATURE]", temperatures[i], 1)
#
#         if word == '[EXCLAMATION]':
#             for i in range(len(exclamations)):
#                 story = story.replace("[EXCLAMATION]", exclamations[i], 1)
#
#         if word == '[UNIT_OF_TIME]':
#             for i in range(len(unit_times)):
#                 story = story.replace("[UNIT_OF_TIME]", unit_times[i], 1)
#
#         if word == '[NICKNAME]':
#             for i in range(len(nicknames)):
#                 story = story.replace("[NICKNAME]", nicknames[i], 1)
#
#         if word == '[NUMBER]':
#             for i in range(len(numbers)):
#                 story = story.replace("[NUMBER]", numbers[i], 1)
#
#         if word == '[LARGE_NUMBER]':
#             for i in range(len(large_numbers)):
#                 story = story.replace("[LARGE_NUMBER]", large_numbers[i], 1)
#
#         if word == '[NAMES_OF_FAMOUS_PEOPLE]':
#             for i in range(len(famous_peoples)):
#                 story = story.replace("[NAMES_OF_FAMOUS_PEOPLE]", famous_peoples[i], 1)
#
#         if word == '[ADJECTIVE]':
#             for i in range(len(adjectives)):
#                 story = story.replace("[ADJECTIVE]", adjectives[i], 1)
#
#         if word == '[ADVERB]':
#             for i in range(len(adverbs)):
#                 story = story.replace("[ADVERB]", adverbs[i], 1)
#
#         if word == '[VERB]':
#             for i in range(len(verbs)):
#                 story = story.replace("[VERB]", verbs[i], 1)
#
#         if word == '[VERB_ENDING_IN_ING]':
#             for i in range(len(verbs_ing)):
#                 story = story.replace("[VERB_ENDING_IN_ING]", verbs_ing[i], 1)
#
#
#     return render(request, 'list/show.html', {'lib': lib, 'story': story, 'result': result})


