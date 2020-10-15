import json


def preprocess(text):
    """ Simple Arabic tokenizer and sentencizer. It is a space-based tokenizer. I use some rules to handle
    tokenition exception like words containing the preposition 'و'. For example 'ووالدته' is tokenized to 'و والدته'

    :param text: Arabic text to handle
    :return: list of tokenized sentences
    """
    try:
        text = text.decode('utf-8')
    except(UnicodeDecodeError, AttributeError):
        pass
    text = text.strip()
    tokenizer_exceptions = ["وظف", "وضعها", "وضعه", "وقفنا", "وصفوها", "وجهوا", "والدته", "والده", "وادي", "وضعية",
                            "واجهات", "وفرتها", "وقاية", "وفا", "وزيرنا", "وزارتي", "وجهاها", "واردة", "وضعته",
                            "وضعتها", "وجاهة", "وهمية", "واجهة", "واضعاً", "واقعي", "ودائع", "واعدا", "واع", "واسعا",
                            "ورائها", "وحدها", "وزارتي", "وزارتي", "والدة", "وزرائها", "وسطاء", "وليامز", "وافق",
                            "والدها", "وسم", "وافق", "وجهها", "واسعة", "واسع", "وزنها", "وزنه",
                            "وصلوا", "والدها", "وصولاً", "وضوحاً", "وجّهته", "وضعته", "ويكيليكس", "وحدها", "وزيراً",
                            "وقفات", "وعر", "واقيًا", "وقوف", "وصولهم", "وارسو", "واجهت", "وقائية", "وضعهم",
                            "وسطاء", "وظيفته", "ورائه", "واسع", "ورط", "وظفت", "وقوف", "وافقت", "وفدًا", "وصلتها",
                            "وثائقي", "ويليان", "وساط", "وُقّع", "وَقّع", "وخيمة", "ويست", "والتر", "وهران", "ولاعة",
                            "ولايت", "والي", "واجب", "وظيفتها", "ولايات", "واشنطن", "واصف",
                            "وقح", "وعد", "وقود", "وزن", "وقوع", "ورشة", "وقائع", "وتيرة", "وساطة", "وفود", "وفات",
                            "وصاية", "وشيك", "وثائق", "وطنية", "وجهات", "وجهت", "وعود", "وضعهم", "وون", "وسعها", "وسعه",
                            "ولاية", "واصفاً", "واصلت", "وليان", "وجدتها", "وجدته", "وديتي", "وطأت", "وطأ", "وعودها",
                            "وجوه", "وضوح", "وجيز", "ورثنا", "ورث", "واقع", "وهم", "واسعاً", "وراثية", "وراثي", "والاس",
                            "واجهنا", "وابل", "ويكيميديا", "واضحا", "واضح", "وصفته", "واتساب", "وحدات", "ون",
                            "وورلد", "والد", "وكلاء", "وتر", "وثيق", "وكالة", "وكالات", "و احدة", "واحد", "وصيته",
                            "وصيه", "ويلمينغتون", "ولد", "وزر", "وعي", "وفد", "وصول", "وقف", "وفاة", "ووتش", "وسط",
                            "وزراء", "وزارة", "ودي", "وصيف", "ويمبلدون", "وست", "وهج", "والد", "وليد", "وثار",
                            "وجد", "وجه", "وقت", "ويلز", "وجود", "وجيه", "وحد", "وحيد", "ودا", "وداد", "ودرو",
                            "ودى", "وديع", "وراء", "ورانس", "ورث", "ورَّث", "ورد", "وردة", "ورق", "ورم", "وزير",
                            "وسام", "وسائل", "وستون", "وسط", "وسن", "وسيط", "وسيلة", "وسيم", "وصاف", "وصف", "وصْفَ",
                            "وصل", "وضع", "وطن", "وعاء", "وفاء", "وفق", "وفيق", "وقت", "وقع", "وكال", "وكيل",
                            "ولاء", "ولف", "وهب", "وباء", "ونستون", "وضح", "وجب", "وقّع", "ولنغتون", "وحش",
                            "وفر", "ولادة", "ولي", "وفيات", "وزار", "وجّه", "وهماً", "وجَّه", "وظيفة", "وظائف", "وقائي"]

    sentence_splitter_exceptions = ["د.", "كي.", "في.", "آر.", "بى.", "جى.", "دى.", "جيه.", "ان.", "ال.", "سى.", "اس.",
                                    "اتش.", "اف."]

    sentence_splitters = ['.', '!', '؟', '\n']
    text = text.replace('،', ' ، ')
    text = text.replace('*', ' * ')
    text = text.replace('’', ' ’ ')
    text = text.replace('‘', ' ‘ ')
    text = text.replace(',', ' , ')
    text = text.replace('(', ' ( ')
    text = text.replace(')', ' ) ')
    text = text.replace('/', ' / ')
    text = text.replace('[', ' [ ')
    text = text.replace(']', ' ] ')
    text = text.replace('|', ' | ')
    text = text.replace('؛', ' ؛ ')
    text = text.replace('«', ' « ')
    text = text.replace('»', ' » ')
    text = text.replace('!', ' ! ')
    text = text.replace('-', ' - ')
    text = text.replace('“', ' “ ')
    text = text.replace('”', ' ” ')
    text = text.replace('"', ' " ')
    text = text.replace('؟', ' ؟ ')
    text = text.replace(':', ' : ')
    text = text.replace('…', ' … ')
    text = text.replace('..', ' .. ')
    text = text.replace('...', ' ... ')
    text = text.replace('\'', ' \' ')
    text = text.replace('\n', ' \n ')
    text = text.replace('  ', ' ')
    tokens = text.split()
    for i, token in enumerate(tokens):
        if token[-1] in sentence_splitters:
            is_exceptions = token in sentence_splitter_exceptions
            if not is_exceptions:
                tokens[i] = token[:-1] + ' ' + token[-1] + 'SENT_SPLITTER'
    tokens = ' '.join(tokens).split()
    for i, token in enumerate(tokens):
        if token.startswith('و'):
            is_exceptions = [token.startswith(exception) and len(token) <= len(exception) + 1 for exception in
                             tokenizer_exceptions]
            if True not in is_exceptions:
                tokens[i] = token[0] + ' ' + token[1:]
    text = (' '.join(tokens))
    text = text.replace(' وال', ' و ال')
    text = text.replace(' لل', ' ل ل')
    text = text.replace(' لإ', ' ل إ')
    text = text.replace(' بالأ', ' ب الأ')
    text = text.replace('وفقا ل', 'وفقا ل ')
    text = text.replace('نسبة ل', 'نسبة ل ')
    sentences = text.split('SENT_SPLITTER')
    return sentences


def postprocess(outputs):
    """ Postprocess the BIO-formatted result

    :param output: list of tokens and their corresponding BIO tags
    :return: json-formatted result
    """
    words = []
    ner_labels = []
    for sentence in outputs:
        for item in sentence:
            words.append(list(item.keys())[0])
            ner_labels.append(item[list(item.keys())[0]])
    text, entities = convert_to_ents_dict(words, ner_labels)
    response = {"text": text, "entities": entities}
    response = json.dumps(response, ensure_ascii=False)
    return response


def convert_to_ents_dict(tokens, tags):
    """ Handle the BIO-formatted data

    :param tokens: list of tokens
    :param tags: list of corresponding BIO tags
    :return: json-formatted result
    
    """
    ent_type = None
    entities = []
    start_char_offset = 0
    end_char_offset = 0
    start_char_entity = 0
    entity_tokens = []
    tokens_length = len(tokens)
    for position, (token, token_tag) in enumerate(zip(tokens, tags)):
        if token_tag == "O":
            if ent_type:
                entity = {
                    "type": ent_type,
                    "entity": " ".join(entity_tokens),
                    "start_offset": start_char_entity + 1,
                    "end_offset": end_char_offset + 1
                }
                entities.append(entity)
            entity_tokens = []
            ent_type = None
        elif ent_type and token_tag.startswith('B-'):
            entity = {
                "type": ent_type,
                "entity": " ".join(entity_tokens),
                "start_offset": start_char_entity + 1,
                "end_offset": end_char_offset + 1
            }
            entities.append(entity)
            entity_tokens = []
            ent_type = token_tag[2:]
            entity_tokens.append(token)
            start_char_entity = len(" ".join(tokens[:position]))
        elif token_tag.startswith('B-'):
            ent_type = token_tag[2:]
            entity_tokens.append(token)
            start_char_entity = len(" ".join(tokens[:position]))
        elif not ent_type and token_tag.startswith('I-'):
            ent_type = token_tag[2:]
            entity_tokens.append(token)
            start_char_entity = len(" ".join(tokens[:position]))
        elif ent_type and token_tag.startswith('I-') and token_tag[2:] == ent_type:
            entity_tokens.append(token)
        elif ent_type and token_tag.startswith('I-') and token_tag[2:] != ent_type:
            entity = {
                "type": ent_type,
                "entity": " ".join(entity_tokens),
                "start_offset": start_char_entity + 1,
                "end_offset": end_char_offset + 1
            }
            entities.append(entity)
            entity_tokens = []
            ent_type = token_tag[2:]
            entity_tokens.append(token)
            start_char_entity = len(" ".join(tokens[:position]))
        if position:
            start_char_offset = len(" ".join(tokens[:position])) + 1
        end_char_offset = start_char_offset + len(token) - 1
        # catches an entity that foes up until the last token
        if ent_type and position == tokens_length - 1:
            entity = {
                "type": ent_type,
                "entity": " ".join(entity_tokens),
                "start_offset": start_char_entity + 1,
                "end_offset": end_char_offset + 1
            }
            entities.append(entity)

    return [" ".join(tokens), entities]
