from PIL import Image, ImageDraw
import math

def draw_balloon(diameter, spacing, divs, output_file):
    # Calcular as dimensões da imagem
    width = diameter * divs + 50 + 2 * spacing
    height = int(diameter * 2.5) + 50 + 2 * spacing
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Desenhar o círculo central
    center_x =diameter // 2 + 5
    center_y =diameter // 2 + 5
    draw.line((center_x , center_y-diameter//2,center_x,center_y  ),fill="black")
    draw.ellipse((center_x - diameter // 2, center_y - diameter // 2, 
                  center_x + diameter // 2, center_y + diameter // 2), outline="black")
    draw.ellipse((center_x - diameter // 2, diameter * 1.7 - diameter // 2, 
                  center_x + diameter // 2, diameter * 1.7  + diameter // 2), outline="black")
    center_x=center_x + center_x
    draw.line((0, center_y,width,center_y  ),fill="black")
    draw.line((0, diameter * 1.7,width,diameter * 1.7  ),fill="black")
    # Desenhar os círculos x
    for i in range(divs):
        
        circle_diameter = diameter - (i + 1) * (diameter // (2 * divs))
        center_x = center_x + circle_diameter
        draw.line((center_x , center_y-circle_diameter//2,center_x,center_y  ),fill="black")
        draw.ellipse((center_x - circle_diameter//2, center_y - circle_diameter//2, 
                  center_x +circle_diameter//2, center_y + circle_diameter//2), outline="black")
    
    center_x =diameter // 2 + 5
    center_y =diameter * 1.7 + 5
    # Desenhar os círculos x
    for i in range(divs):
        
        circle_diameter = diameter - (i + 1) * (diameter // (2 * divs))
        center_x = center_x + circle_diameter
        draw.line((center_x , center_y+circle_diameter//2,center_x,center_y  ),fill="black")
        draw.ellipse((center_x - circle_diameter//2, center_y - circle_diameter//2, 
                  center_x +circle_diameter//2, center_y + circle_diameter//2), outline="black")
                  
    

    # Salvar a imagem
    image.save(output_file)
    print(f"Imagem salva como {output_file}")

def main():
    # Perguntar ao usuário as dimensões
    try:
        diameter = int(input("Enter the diameter of the central circle in pixels: "))
        spacing = int(input("Enter the spacing around the circle in pixels: "))
        divs = int(input("Enter the number of divisions: "))
    except ValueError:
        print("Please enter valid integer values.")
        return

    if diameter <= 0 or spacing < 0 or divs <= 0:
        print("Diameter, spacing, and divisions must be positive integers.")
        return

    # Desenhar o balão
    draw_balloon(diameter, spacing, divs, "balloon.png")

print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

