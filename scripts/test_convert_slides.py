import pytest
from scripts.convert_slides import remove_watermark

def test_remove_watermark_basic():
    html_content = '''
    <div>
        <text>Some valid text</text>
        <text style="color:red;">Evaluation only. Created with Aspose.Slides for Python via .NET 23.9.</text>
        <text>More valid text</text>
    </div>
    '''
    expected = '''
    <div>
        <text>Some valid text</text>
        <text>More valid text</text>
    </div>
    '''
    assert remove_watermark(html_content) == expected

def test_remove_watermark_no_watermark():
    html_content = '''
    <div>
        <text>Some valid text</text>
        <text>More valid text</text>
    </div>
    '''
    assert remove_watermark(html_content) == html_content

def test_remove_watermark_multiple_watermarks():
    html_content = '''
    <div>
        <text>Evaluation only text 1</text>
        <text>Valid text</text>
        <text>Evaluation only text 2</text>
    </div>
    '''
    expected = '''
    <div>
        <text>Valid text</text>
    </div>
    '''
    assert remove_watermark(html_content) == expected

def test_remove_watermark_multiline():
    html_content = '''
    <text>
        Evaluation only
        over multiple lines
    </text>
    '''
    expected = '''
    '''
    assert remove_watermark(html_content) == expected

def test_remove_watermark_custom_text():
    html_content = '''
    <div>
        <text>Some valid text</text>
        <text style="color:blue;">Custom Watermark Text to Remove</text>
        <text>More valid text</text>
    </div>
    '''
    expected = '''
    <div>
        <text>Some valid text</text>
        <text>More valid text</text>
    </div>
    '''
    assert remove_watermark(html_content, watermark_text="Custom Watermark Text") == expected
