import sys
import requests

import pypdfium2 as pdfium

DPI = 200

AREAS = [
    (0, 0, 827, 1160),
    (828, 0, 1654, 1160),
    (0, 1161, 827, 2321),
    (828, 1161, 1654, 2321),
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    }

IMAGE_QUALITY = 20


def main():
    args = sys.argv[1:]

    url_pdf, output_path = None, None

    for i in range(0, len(args), 2):
        parametrName = args[i]
        if parametrName == '-url_pdf':
            url_pdf = args[i+1]
        if parametrName == '-output_path':
            output_path = args[i+1]

    if url_pdf is None or output_path is None:
        raise Exception('Not definite required  parametrs url_pdf/output_path')

    convert_to_image(url_pdf, output_path)


def convert_to_image(url_pdf: str, output_path: str):

    response = requests.get(url_pdf, headers=HEADERS)
    if response.status_code != 200:
        raise Exception('Could not download pdf file')

    pdf = pdfium.PdfDocument(response.content)

    page_indices = [i for i in range(len(pdf))]
    renderer = pdf.render_to(
        pdfium.BitmapConv.pil_image,
        page_indices=page_indices,
        scale=DPI/72,
    )

    stickers = []

    for image in renderer:

        for area in AREAS:

            cropped_image = image.crop(area)

            extrema = cropped_image.convert("L").getextrema()
            if extrema == (255, 255):
                continue

            stickers.append(cropped_image)

    for i, sticker in zip(range(len(stickers)), stickers):
        sticker.save(f'{output_path}out_{i}.jpg', IMAGE_QUALITY=20,
                     optimize=True)


if __name__ == "__main__":
    main()
