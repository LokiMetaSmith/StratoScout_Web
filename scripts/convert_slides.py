import aspose.slides as slides
import os
import argparse
import sys
import re

def remove_watermark(html_content: str, watermark_text: str = "Evaluation only") -> str:
    """Removes the specified watermark from the given HTML content."""
    escaped_text = re.escape(watermark_text)
    pattern = re.compile(rf'[ \t]*<text[^>]*>(?:(?!</text>).)*?{escaped_text}(?:(?!</text>).)*?</text>[ \t]*\n?', re.DOTALL)
    return pattern.sub('', html_content)

def convert_pptx_to_html_slides(pptx_path, output_dir, watermark_text="Evaluation only"):
    if not os.path.exists(pptx_path):
        print(f"Error: The input file '{pptx_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Loading presentation from {pptx_path}...")
    try:
        presentation = slides.Presentation(pptx_path)

        # Use HTML options
        options = slides.export.HtmlOptions()
        options.html_formatter = slides.export.HtmlFormatter.create_document_formatter("", False)

        for i, slide in enumerate(presentation.slides):
            slide_num = i + 1
            output_file = os.path.join(output_dir, f"slide_{slide_num}.html")
            print(f"Exporting Slide {slide_num} to {output_file}...")

            presentation.save(output_file, [slide_num], slides.export.SaveFormat.HTML, options)

            # Post-processing: remove the watermark from the generated HTML
            with open(output_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            cleaned_content = remove_watermark(html_content, watermark_text=watermark_text)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)

        print("All slides converted and cleaned successfully!")
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing the presentation.\nDetails: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert PPTX to HTML slides and remove Aspose watermark.")
    parser.add_argument("--input", default="StratoScout Public Sector Pitch Deck.pptx", help="Path to the input PPTX file.")
    parser.add_argument("--output", default="slides_html", help="Directory to save the output HTML slides.")
    parser.add_argument("--watermark-text", default="Evaluation only", help="Text of the watermark to remove.")

    args = parser.parse_args()

    convert_pptx_to_html_slides(args.input, args.output, args.watermark_text)

if __name__ == "__main__":
    main()
