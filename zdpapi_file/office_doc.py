from docx import Document


def get_word_info(document):
    """
    获取文档的属性
    :param document:
    :return:
    """
    core_properties = document.core_properties

    # print('作者:', core_properties.author)
    # print('创建时间', core_properties.created)
    # print(core_properties.last_modified_by)
    # print(core_properties.last_printed)
    # print(core_properties.modified)
    # print(core_properties.revision)
    # print(core_properties.title)
    # print(core_properties.category)
    # print(core_properties.comments)
    # print(core_properties.identifier)
    # print(core_properties.keywords)
    # print(core_properties.language)
    # print(core_properties.subject)
    # print(core_properties.version)
    # print(core_properties.keywords)
    # print(core_properties.content_status)
    created = core_properties.created
    if created is not None:
        created = created.strftime('%Y-%m-%d %H:%M:%S')
    last_printed = core_properties.last_printed
    if last_printed is not None:
        last_printed = last_printed.strftime('%Y-%m-%d %H:%M:%S')
    modified = core_properties.modified
    if modified is not None:
        modified = modified.strftime('%Y-%m-%d %H:%M:%S')
    return {'作者': core_properties.author, '创建时间': created,
            '最后修改人': core_properties.last_modified_by,
            '最后打印时间': last_printed, '最后修改时间': modified}


if __name__ == '__main__':
    file = "D:\\BaiduNetdiskWorkspace\\文档\\编程语言\\Python\\测试\\张大鹏pytest教程.docx"
    file = Document(file)
    print(get_word_info(file))
