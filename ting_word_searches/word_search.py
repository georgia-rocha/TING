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
    pass
