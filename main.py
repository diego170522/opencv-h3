# GITHUB
# https://github.com/diego170522/opencv-h3

import os
import shutil
import cv2
from zipfile import ZipFile
from urllib.request import urlretrieve


class Colores:
    RESET = "\033[0m"
    NEGRO = "\033[30m"
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BLANCO = "\033[37m"


def imprimir_mensaje_coloreado(mensaje, color):
    print(color + mensaje + Colores.RESET)


def copiarImagenes():
    def copiar_archivo(ruta_origen, ruta_destino):
        try:
            shutil.copy(ruta_origen, ruta_destino)
            print("El archivo se ha copiado exitosamente.")
        except FileNotFoundError:
            print("Error: El archivo no ha sido encontrado.")
        except PermissionError:
            print("Error: Permiso denegado.")
        except Exception as e:
            print("Error:", e)

    def main():
        print("Aplicación de copia de archivos")
        ruta_origen = input(
            r"Ingrese la ruta del archivo a copiar. Ej.: C:\Users\Mauricio\Desktop\prueba\imagen.png: "
        )
        ruta_destino = input(
            r"Ingrese la ruta de destino para la copia. Ej.: C:\Users\Mauricio\Desktop\imagenes: "
        )

        copiar_archivo(ruta_origen, ruta_destino)
        # Leer la imagen con OpenCV
        imagen = cv2.imread(ruta_origen)

        # Verificar si la imagen se cargó correctamente
        if imagen is None:
            print("Error: No se pudo cargar la imagen.")
            return

        # Obtener el ancho, altura y cantidad de canales de colores de la imagen
        altura, ancho, canales = imagen.shape

        # Mostrar la información
        print("Ancho de la imagen:", ancho)
        print("Altura de la imagen:", altura)
        print("Canales de colores de la imagen:", canales)

    if __name__ == "__main__":
        main()


def caracteristicasImagen():
    # Solicitar al usuario que ingrese la ruta de la imagen
    ruta_imagen = input("Por favor, ingrese la ruta de la imagen: ")

    # Leer la imagen con OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    # Obtener el ancho, altura y cantidad de canales de colores de la imagen
    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Mostrar la imagen utilizando OpenCV
    # cv2.imshow("Imagen", imagen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def invertir_imagen():
    # Solicitar al usuario que ingrese la ruta de la imagen
    ruta_imagen = input("Por favor, ingrese la ruta de la imagen: ")

    # Leer la imagen con OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Solicitar al usuario que elija la dirección de inversión
    direccion = input(
        "¿Desea invertir la imagen horizontalmente o verticalmente? (h/v): "
    )

    # Verificar la opción seleccionada por el usuario y realizar la inversión correspondiente
    if direccion.lower() == "h":
        imagen_invertida = cv2.flip(imagen, 1)  # Invertir horizontalmente
        print("La imagen se ha invertido horizontalmente.")
    elif direccion.lower() == "v":
        imagen_invertida = cv2.flip(imagen, 0)  # Invertir verticalmente
        print("La imagen se ha invertido verticalmente.")
    else:
        print(
            "Opción no válida. Por favor, seleccione 'h' para invertir horizontalmente o 'v' para invertir verticalmente."
        )
        return

    # Crear una ventana con el nombre "Imagen Invertida" y maximizarla
    cv2.namedWindow("Imagen Invertida", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(
        "Imagen Invertida", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL
    )

    # Mostrar la imagen invertida utilizando OpenCV
    cv2.imshow("Imagen Invertida", imagen_invertida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def sobrescribir_pixeles():
    # Solicitar al usuario que ingrese la ruta de la imagen
    ruta_imagen = input("Por favor, ingrese la ruta de la imagen: ")

    # Leer la imagen con OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Obtener las dimensiones de la imagen
    altura, ancho, _ = imagen.shape

    # Solicitar al usuario que ingrese las coordenadas (x1, y1) y (x2, y2)
    x1 = int(input("Ingrese la coordenada x1: "))
    y1 = int(input("Ingrese la coordenada y1: "))
    x2 = int(input("Ingrese la coordenada x2: "))
    y2 = int(input("Ingrese la coordenada y2: "))

    # Verificar si las coordenadas están dentro de los límites de la imagen
    if (
        x1 < 0
        or x1 >= ancho
        or x2 < 0
        or x2 >= ancho
        or y1 < 0
        or y1 >= altura
        or y2 < 0
        or y2 >= altura
    ):
        print("Error: Las coordenadas están fuera de los límites de la imagen.")
        return

    # Solicitar al usuario que ingrese el color del rectángulo en formato RGB
    print("Color de la figura:")
    color_r = int(input("Ingrese el valor de R (0-255): "))
    color_g = int(input("Ingrese el valor de G (0-255): "))
    color_b = int(input("Ingrese el valor de B (0-255): "))

    # Pintar el área definida por las coordenadas con el color especificado
    color_rectangulo = (color_b, color_g, color_r)  # OpenCV utiliza BGR en lugar de RGB
    imagen_pintada = imagen.copy()
    cv2.rectangle(
        imagen_pintada, (x1, y1), (x2, y2), color_rectangulo, thickness=cv2.FILLED
    )

    # Mostrar la imagen resultante

    # Crear una ventana con el nombre "Imagen Invertida" y maximizarla
    cv2.namedWindow("Imagen Invertida", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(
        "Imagen Invertida", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL
    )

    # Mostrar la imagen invertida utilizando OpenCV
    cv2.imshow("Imagen Invertida", imagen_pintada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ampliar_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen usando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Pedir al usuario el factor de modificación
    try:
        factor_modificacion = float(
            input("Ingrese el factor de modificación (-10 a 10): ")
        )
    except ValueError:
        print("Por favor, ingrese un número válido para el factor de modificación.")
        return

    # Verificar si el factor de modificación está dentro del rango permitido
    if factor_modificacion < -10 or factor_modificacion > 10:
        print("El factor de modificación debe estar en el rango de -10 a 10.")
        return

    # Calcular el factor de ampliación o reducción según el valor proporcionado
    if factor_modificacion >= 0:
        factor_ampliacion = factor_modificacion + 1
    else:
        factor_ampliacion = 1 / abs(
            factor_modificacion
        )  # Invierte y toma el valor absoluto

    # Modificar la imagen según el factor de ampliación o reducción
    imagen_modificada = cv2.resize(
        imagen, None, fx=factor_ampliacion, fy=factor_ampliacion
    )

    # Mostrar la imagen modificada en una ventana
    cv2.imshow("Imagen Modificada", imagen_modificada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def recortar_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen utilizando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    # Mostrar la altura y la anchura de la imagen
    altura, anchura, _ = imagen.shape
    print(f"Altura de la imagen: {altura} píxeles")
    print(f"Anchura de la imagen: {anchura} píxeles")

    # Pedir al usuario las coordenadas para el recorte
    x1 = int(input("Ingrese la coordenada x1 del punto superior izquierdo: "))
    y1 = int(input("Ingrese la coordenada y1 del punto superior izquierdo: "))
    x2 = int(input("Ingrese la coordenada x2 del punto inferior derecho: "))
    y2 = int(input("Ingrese la coordenada y2 del punto inferior derecho: "))

    # Realizar el recorte de la imagen
    imagen_recortada = imagen[y1:y2, x1:x2]

    # Mostrar el resultado en una ventana
    cv2.imshow("Imagen Recortada", imagen_recortada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def insertar_texto_en_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen utilizando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    # Obtener el ancho, altura y cantidad de canales de colores de la imagen
    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Pedir al usuario el texto a insertar
    texto = input("Ingrese el texto a insertar: ")

    # Pedir al usuario las coordenadas donde ubicar el texto
    try:
        x = int(input("Ingrese la coordenada x para la ubicación del texto: "))
        y = int(input("Ingrese la coordenada y para la ubicación del texto: "))
    except ValueError:
        print("Por favor, ingrese valores válidos para las coordenadas.")
        return

    # Pedir al usuario el color del texto en formato RGB
    try:
        color_r = int(input("Ingrese el valor de R (0-255): "))
        color_g = int(input("Ingrese el valor de G (0-255): "))
        color_b = int(input("Ingrese el valor de B (0-255): "))
    except ValueError:
        print("Por favor, ingrese valores válidos para los componentes RGB.")
        return

    # Definir el tamaño de la fuente y el color del texto
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    escala = 1  # Escala de la fuente
    grosor = 2  # Grosor del texto
    color_texto = (color_b, color_g, color_r)  # Color del texto en formato BGR

    # Insertar el texto en la imagen en las coordenadas especificadas
    imagen_con_texto = cv2.putText(
        imagen, texto, (x, y), fuente, escala, color_texto, grosor
    )

    # Mostrar el resultado en una ventana
    cv2.imshow("Imagen con Texto", imagen_con_texto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dibujar_rectangulo_sobre_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen utilizando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Pedir al usuario las coordenadas del rectángulo
    try:
        x1 = int(input("Ingrese la coordenada x1 del vértice superior izquierdo: "))
        y1 = int(input("Ingrese la coordenada y1 del vértice superior izquierdo: "))
        x2 = int(input("Ingrese la coordenada x2 del vértice inferior derecho: "))
        y2 = int(input("Ingrese la coordenada y2 del vértice inferior derecho: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos para las coordenadas.")
        return

    # Verificar si las coordenadas del rectángulo son válidas
    if x1 >= x2 or y1 >= y2:
        print("Las coordenadas del rectángulo no son válidas.")
        return

    # Pedir al usuario el color del rectángulo en formato RGB
    try:
        color_r = int(input("Ingrese el valor de R (0-255): "))
        color_g = int(input("Ingrese el valor de G (0-255): "))
        color_b = int(input("Ingrese el valor de B (0-255): "))
    except ValueError:
        print("Por favor, ingrese valores válidos para los componentes RGB.")
        return

    # Verificar si los valores RGB están en el rango permitido
    if not (0 <= color_r <= 255 and 0 <= color_g <= 255 and 0 <= color_b <= 255):
        print("Los valores RGB deben estar en el rango de 0 a 255.")
        return

    # Definir el color del rectángulo (en BGR)
    color_rectangulo = (color_b, color_g, color_r)

    # Dibujar el rectángulo sobre la imagen
    imagen_con_rectangulo = cv2.rectangle(
        imagen, (x1, y1), (x2, y2), color_rectangulo, thickness=2
    )

    # Mostrar el resultado en una ventana
    cv2.imshow("Imagen con Rectángulo", imagen_con_rectangulo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dibujar_linea_sobre_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen utilizando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Pedir al usuario las coordenadas de los puntos para dibujar la línea
    try:
        x1 = int(input("Ingrese la coordenada x del primer punto: "))
        y1 = int(input("Ingrese la coordenada y del primer punto: "))
        x2 = int(input("Ingrese la coordenada x del segundo punto: "))
        y2 = int(input("Ingrese la coordenada y del segundo punto: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos para las coordenadas.")
        return

    # Pedir al usuario el color de la línea en formato RGB
    try:
        color_r = int(input("Ingrese el valor de R (0-255): "))
        color_g = int(input("Ingrese el valor de G (0-255): "))
        color_b = int(input("Ingrese el valor de B (0-255): "))
    except ValueError:
        print("Por favor, ingrese valores válidos para los componentes RGB.")
        return

    # Verificar si los valores RGB están en el rango permitido
    if not (0 <= color_r <= 255 and 0 <= color_g <= 255 and 0 <= color_b <= 255):
        print("Los valores RGB deben estar en el rango de 0 a 255.")
        return

    # Definir el color de la línea (en BGR)
    color_linea = (color_b, color_g, color_r)

    # Dibujar la línea sobre la imagen
    imagen_con_linea = cv2.line(imagen, (x1, y1), (x2, y2), color_linea, thickness=2)

    # Mostrar el resultado en una ventana
    cv2.imshow("Imagen con Línea", imagen_con_linea)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dibujar_circulo_sobre_imagen():
    # Pedir al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    # Leer la imagen utilizando OpenCV
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
        return

    altura, ancho, canales = imagen.shape

    # Mostrar la información
    print("Ancho de la imagen:", ancho)
    print("Altura de la imagen:", altura)
    print("Canales de colores de la imagen:", canales)

    # Pedir al usuario las coordenadas del centro del círculo y su radio
    try:
        x = int(input("Ingrese la coordenada x del centro del círculo: "))
        y = int(input("Ingrese la coordenada y del centro del círculo: "))
        radio = int(input("Ingrese el radio del círculo: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos para las coordenadas y el radio.")
        return

    # Pedir al usuario el color del círculo en formato RGB
    try:
        color_r = int(input("Ingrese el valor de R (0-255): "))
        color_g = int(input("Ingrese el valor de G (0-255): "))
        color_b = int(input("Ingrese el valor de B (0-255): "))
    except ValueError:
        print("Por favor, ingrese valores válidos para los componentes RGB.")
        return

    # Verificar si los valores RGB están en el rango permitido
    if not (0 <= color_r <= 255 and 0 <= color_g <= 255 and 0 <= color_b <= 255):
        print("Los valores RGB deben estar en el rango de 0 a 255.")
        return

    # Definir el color del círculo (en BGR)
    color_circulo = (color_b, color_g, color_r)

    # Dibujar el círculo sobre la imagen
    imagen_con_circulo = cv2.circle(imagen, (x, y), radio, color_circulo, thickness=2)

    # Mostrar el resultado en una ventana
    cv2.imshow("Imagen con Círculo", imagen_con_circulo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def reconocimiento_facial():
    # ========================-Downloading Assets-========================
    def download_and_unzip(url, save_path):
        print(f"Downloading and extracting assests....", end="")

        # Downloading zip file using urllib package.
        urlretrieve(url, save_path)

        try:
            # Extracting zip file using the zipfile package.
            with ZipFile(save_path) as z:
                # Extract ZIP file contents in the same directory.
                z.extractall(os.path.split(save_path)[0])

            print("Done")

        except Exception as e:
            print("\nInvalid file.", e)

    URL = (
        r"https://www.dropbox.com/s/efitgt363ada95a/opencv_bootcamp_assets_12.zip?dl=1"
    )

    asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_12.zip")

    # Download if assest ZIP does not exists.
    if not os.path.exists(asset_zip_path):
        download_and_unzip(URL, asset_zip_path)
    # ====================================================================

    # s = 0
    # if len(sys.argv) > 1:
    #    s = sys.argv[1]

    source = cv2.VideoCapture(0)

    win_name = "Camera Preview"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    net = cv2.dnn.readNetFromCaffe(
        "deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel"
    )
    # Model parameters
    in_width = 300
    in_height = 300
    mean = [104, 117, 123]
    conf_threshold = 0.7

    while cv2.waitKey(1) != 27:
        has_frame, frame = source.read()
        if not has_frame:
            break
        frame = cv2.flip(frame, 1)
        # frame[10:220,10:200] = [255,255,255]
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]

        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(
            frame, 1.0, (in_width, in_height), mean, swapRB=False, crop=False
        )
        # Run a model
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
                y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
                x_right_top = int(detections[0, 0, i, 5] * frame_width)
                y_right_top = int(detections[0, 0, i, 6] * frame_height)

                cv2.rectangle(
                    frame,
                    (x_left_bottom, y_left_bottom),
                    (x_right_top, y_right_top),
                    (0, 255, 0),
                )
                label = "Confidence: %.4f" % confidence
                label_size, base_line = cv2.getTextSize(
                    label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
                )

                cv2.rectangle(
                    frame,
                    (x_left_bottom, y_left_bottom - label_size[1]),
                    (x_left_bottom + label_size[0], y_left_bottom + base_line),
                    (255, 255, 255),
                    cv2.FILLED,
                )
                cv2.putText(
                    frame,
                    label,
                    (x_left_bottom, y_left_bottom),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                )

        t, _ = net.getPerfProfile()
        label = "Inference time: %.2f ms" % (t * 1000.0 / cv2.getTickFrequency())
        cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)
    print("Finito")


def mostrar_menu():
    imprimir_mensaje_coloreado(r"██████╗ ██╗███████╗ ██████╗  ██████╗ ", Colores.VERDE)
    imprimir_mensaje_coloreado(r"██╔══██╗██║██╔════╝██╔════╝ ██╔═══██╗", Colores.VERDE)
    imprimir_mensaje_coloreado(r"██║  ██║██║█████╗  ██║  ███╗██║   ██║", Colores.VERDE)
    imprimir_mensaje_coloreado(r"██║  ██║██║██╔══╝  ██║   ██║██║   ██║", Colores.VERDE)
    imprimir_mensaje_coloreado(r"██████╔╝██║███████╗╚██████╔╝╚██████╔╝", Colores.VERDE)
    imprimir_mensaje_coloreado(r"╚═════╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ", Colores.VERDE)
    imprimir_mensaje_coloreado(
        r"███╗   ███╗███████╗███╗   ██╗██████╗  ██████╗ ███████╗ █████╗ ", Colores.VERDE
    )
    imprimir_mensaje_coloreado(
        r"████╗ ████║██╔════╝████╗  ██║██╔══██╗██╔═══██╗╚══███╔╝██╔══██╗", Colores.VERDE
    )
    imprimir_mensaje_coloreado(
        r"██╔████╔██║█████╗  ██╔██╗ ██║██║  ██║██║   ██║  ███╔╝ ███████║", Colores.VERDE
    )
    imprimir_mensaje_coloreado(
        r"██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║  ██║██║   ██║ ███╔╝  ██╔══██║", Colores.VERDE
    )
    imprimir_mensaje_coloreado(
        r"██║ ╚═╝ ██║███████╗██║ ╚████║██████╔╝╚██████╔╝███████╗██║  ██║", Colores.VERDE
    )
    imprimir_mensaje_coloreado(
        r"╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝", Colores.VERDE
    )
    imprimir_mensaje_coloreado("Menú de opciones:", Colores.VERDE)
    imprimir_mensaje_coloreado("1. Copiar Imágenes", Colores.VERDE)
    imprimir_mensaje_coloreado(
        "2. Mostrar características de una imagen", Colores.VERDE
    )
    imprimir_mensaje_coloreado("3. Sobrescribir los pixeles", Colores.VERDE)
    imprimir_mensaje_coloreado("4. Invertir una imagen", Colores.VERDE)
    imprimir_mensaje_coloreado("5. Ampliar o reducir una imagen", Colores.VERDE)
    imprimir_mensaje_coloreado("6. Recortar una imagen", Colores.VERDE)
    imprimir_mensaje_coloreado("7. Escribir texto en la imagen", Colores.VERDE)
    imprimir_mensaje_coloreado("8. Dibujar elementos en una imagen", Colores.VERDE)
    imprimir_mensaje_coloreado("9. Reconocimiento facial", Colores.VERDE)
    imprimir_mensaje_coloreado("0. Salir", Colores.VERDE)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una operación: ")

        if opcion == "1":
            copiarImagenes()
        elif opcion == "2":
            caracteristicasImagen()
        elif opcion == "3":
            sobrescribir_pixeles()
        elif opcion == "4":
            invertir_imagen()
        elif opcion == "5":
            ampliar_imagen()
        elif opcion == "6":
            recortar_imagen()
        elif opcion == "7":
            insertar_texto_en_imagen()
        elif opcion == "8":
            # dibujar_figura_sobre_imagen()
            # dibujar_rectangulo_sobre_imagen()
            print("1. Línea")
            print("2. Rectángulo")
            print("3. Círculo")
            figura = input("Seleccionar una figura: ")
            if figura == "1":
                dibujar_linea_sobre_imagen()
            elif figura == "2":
                dibujar_rectangulo_sobre_imagen()
            elif figura == "3":
                dibujar_circulo_sobre_imagen()
            else:
                print("Opción no válida.")
        elif opcion == "9":
            reconocimiento_facial()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
