#!/usr/bin/env python
import Parser
import json
import nltk
from nltk.corpus import brown

def generate_copy_pasta(json_string):
    parsed_list = json.loads(json_string)
    navy_seals_pasta = """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""
    print(type(brown))
    parser = Parser.Parser(brown, *parsed_list)
    result = parser.replace_indices([12, 13, 25, 28, 29, 37, 38, 39, 41, 49, 54, 61, 65, 66, 67, 76, 85, 97, 110, 112, 117, 122, 130, 133, 139, 142, 151, 153, 155, 160, 161, 166, 170, 172, 183, 197, 198, 206, 207, 216, 221, 222, 235, 236, 242, 245, 246, 254, 255, 259, 260], navy_seals_pasta)
    print(result)
    return result


def main():
    parsed_list = [["fight", "combat", "army", "military"], ["bird", "crow", "jackdaw"]]
    navy_seals_pasta = """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""
    parser = Parser.Parser(brown, *parsed_list)
    result = parser.replace_indices([12, 13, 25, 28, 29, 37, 38, 39, 41, 49, 54, 61, 65, 66, 67, 76, 85, 97, 110, 112, 117, 122, 130, 133, 139, 142, 151, 153, 155, 160, 161, 166, 170, 172, 183, 197, 198, 206, 207, 216, 221, 222, 235, 236, 242, 245, 246, 254, 255, 259, 260], navy_seals_pasta)
    print(result)
    
if __name__ == '__main__':
    main()