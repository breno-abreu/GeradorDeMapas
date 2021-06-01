package ptg.generators;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class MapSaver {
    public void matrix2Img(double[][] matrix, int width, int heidth, String url){
        try {
            BufferedImage img = new BufferedImage(width, heidth, BufferedImage.TYPE_3BYTE_BGR);
            for (int i = 0; i < heidth; i++) {
                for (int j = 0; j < width; j++) {
                    int v = (int) (matrix[i][j] * 255);
                    Color color = new Color(v, v, v);
                    img.setRGB(j, i, color.getRGB());
                }
            }
            File output = new File(url);
            ImageIO.write(img, "png", output);
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }

    public void saveMap(BufferedImage img, String url){
        try{
            File output = new File(url);
            ImageIO.write(img, "png", output);
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
}
