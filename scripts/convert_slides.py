import aspose.slides as slides
import os

def convert_pptx_to_html_slides(pptx_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Loading presentation from {pptx_path}...")
    presentation = slides.Presentation(pptx_path)

    # Use HTML options
    options = slides.export.HtmlOptions()
    options.html_formatter = slides.export.HtmlFormatter.create_document_formatter("", False)

    for i, slide in enumerate(presentation.slides):
        slide_num = i + 1
        output_file = os.path.join(output_dir, f"slide_{slide_num}.html")
        print(f"Exporting Slide {slide_num} to {output_file}...")

        presentation.save(output_file, [slide_num], slides.export.SaveFormat.HTML, options)

    print("All slides converted successfully!")

if __name__ == "__main__":
    pptx_file = "StratoScout Public Sector Pitch Deck.pptx"
    output_directory = "slides_html"
    convert_pptx_to_html_slides(pptx_file, output_directory)
