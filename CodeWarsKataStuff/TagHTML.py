def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags, from Fluent Python, page 155"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(f' {attr}="{value}"'
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join(f'<{name}{attr_str}>{c}</{name}>'
                         for c in content)
    else:
        return f'<{name}{attr_str} />'


"""
Examples:

tag('br')
    '<br/>'
tag('p', 'hello', 'yeahhh')
tag('p', 'hello', id=33)
print(tag('p', 'hello', 'world', cls='sidebar'))
tag(content='testing', name="img")
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
            'src': 'Sunset.jpg', 'cls': 'framed'}

tag(**my_tag)
>>>'<img class="framed" src="Sunset.jpg" title="Sunset Boulevard" />'
"""
