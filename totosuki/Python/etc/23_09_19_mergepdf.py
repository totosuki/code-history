import pypdf
merger = pypdf.PdfMerger()
PATH = "/write/to/path"
merger.append(f"{PATH}/1.pdf")
merger.append(f"{PATH}/2.pdf")
merger.write(f"{PATH}/3.pdf")
merger.close()