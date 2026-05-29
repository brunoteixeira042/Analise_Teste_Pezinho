import os
import json
import base64
import glob

def extract_images():
    """
    Lê todos os arquivos Jupyter Notebook (.ipynb) no diretório raiz,
    extrai as imagens PNG incorporadas nos outputs das células de código
    e as salva na pasta 'images/'.
    """
    # Cria a pasta de imagens se não existir
    os.makedirs('images', exist_ok=True)
    print("Iniciando extração de imagens dos notebooks...")

    notebooks = sorted(glob.glob('*.ipynb'))
    if not notebooks:
        print("Nenhum notebook (.ipynb) encontrado no diretório atual.")
        return

    for fn in notebooks:
        print(f"Processando {fn}...")
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                nb = json.load(f)
        except Exception as e:
            print(f"Erro ao abrir {fn}: {e}")
            continue

        img_idx = 1
        cells = nb.get('cells', [])
        for cell in cells:
            if cell.get('cell_type') == 'code':
                outputs = cell.get('outputs', [])
                for out in outputs:
                    if 'data' in out and 'image/png' in out['data']:
                        png_data = out['data']['image/png']
                        # Remove quebras de linha caso existam no base64
                        if isinstance(png_data, list):
                            png_data = "".join(png_data)
                        png_data = png_data.replace('\n', '')

                        try:
                            img_bytes = base64.b64decode(png_data)
                            base_name = os.path.splitext(fn)[0]
                            img_name = f"images/{base_name}_plot_{img_idx}.png"
                            
                            with open(img_name, 'wb') as img_f:
                                img_f.write(img_bytes)
                            
                            print(f"  -> Salvo: {img_name}")
                            img_idx += 1
                        except Exception as e:
                            print(f"  -> Erro ao salvar imagem no notebook {fn}: {e}")

    print("\nExtração finalizada! As imagens estão prontas na pasta 'images/'.")

if __name__ == '__main__':
    extract_images()
