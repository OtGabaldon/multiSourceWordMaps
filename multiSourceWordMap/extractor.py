from pdfminer.high_level import extract_text
import requests
import re
from bs4 import BeautifulSoup
from multiSourceWordMap.configEditor import ConfigEditor
from multiSourceWordMap.utils import create_text_file_path, create_pdf_file_path, is_website

class Extractor:

    def __init__(self, args):
        self.config = ConfigEditor().config
        self.source = args.source # path for pdf, url for website
        self.ticker = args.ticker
        return

    def pull_text_from_source(self):
        if is_website(self.source):
            self.extract_from_website_to_text()
        else:
            self.extract_from_pdf_to_text()           

    def pull_text_for_ticker(self):
        ticker_sources = self.config["sources"][self.ticker]
        for source in ticker_sources:
            self.source = source
            self.pull_text_from_source()
            
    def extract_from_pdf_to_text(self):
        pdf_path = create_pdf_file_path(
            self.config["package_dir"],
            self.ticker,
            self.source
        )
        print(f"Opening PDF: {pdf_path}")
        form_feed = re.compile('')
        non_alpha_numeric = re.compile('[^a-zA-Z ]')
        text = form_feed.sub('', extract_text(pdf_path))
        filtered_text = non_alpha_numeric.sub('', text)
        outPath = create_text_file_path(
                self.config["package_dir"],
                self.ticker,
                self.source
            )
        textOutFile = open(outPath,"w+")
        print(f"Writing to text file: {outPath}")
        textOutFile.write(filtered_text)
        textOutFile.close()

    def extract_from_website_to_text(self):
        doc = requests.get(self.source).text
        outPath = create_text_file_path(
            self.config["package_dir"],
            self.ticker,
            self.source
        )
        textOutFile = open(outPath,"w+")
        textOutFile.write(doc)
        textOutFile.close()



