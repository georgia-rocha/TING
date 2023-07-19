from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    occurrences = []

    if not len(instance):
        return None

    def find_word_in_lines(lines):
        return [{"linha": i} for i, line in enumerate(lines, 1)
                if word.lower() in line.lower()]

    occurrences = [{
        "palavra": word,
        "arquivo": file,
        "ocorrencias": find_word_in_lines(txt_importer(file))
    } for file in instance.queue if
        any(find_word_in_lines(txt_importer(file)))]

    return occurrences


def search_by_word(word, instance):
    occurrences = []

    if not instance.queue:
        return None

    for file in instance.queue:
        file_processing = txt_importer(file)
        occurrences_in_file = [
            {"linha": line_number, "conteudo": line.rstrip()}
            for line_number, line in enumerate(file_processing, 1)
            if word.lower() in line.lower()
        ]

        if occurrences_in_file:
            file_info = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences_in_file
            }
            occurrences.append(file_info)

    return occurrences
