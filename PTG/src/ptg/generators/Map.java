package ptg.generators;
import ptg.generators.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class Map {

    private double[] layersElevation;
    private String[] layersColor;
    private double[][] noiseMatrix;
    private final int width;
    private final int heidth;
    private BufferedImage image;

    public Map(){
        layersElevation = new double[7];
        layersColor = new String[7];
        width = 800;
        heidth = 800;
        image = new BufferedImage(width, heidth, BufferedImage.TYPE_3BYTE_BGR);
    }

    public void generateNoiseMap(long seed, double freq, int octaves) throws Exception{
        Generator generator = new Generator(width, heidth);
        generator.setSeed(seed);

        try {
            generator.setFreq(freq);
            generator.setOctaves(octaves);
        }
        catch(Exception ex){
            throw new Exception(ex.getMessage());
        }

        noiseMatrix = generator.getNoiseMatrix();
        MapSaver saver = new MapSaver();
        saver.matrix2Img(noiseMatrix, width, heidth, "temp/img.png");
    }

    public void setLayers(int index, double elevation, String color){
        layersElevation[index] = elevation;
        layersColor[index] = color;
    }

    public void generateElevationMap(){
        Color color = new Color(0, 0, 0);
        for(int i = 0; i < heidth; i++) {
            for (int j = 0; j < width; j++) {
                for (int e = 0; e < 8; e++) {
                    if (e == 0) {
                        if (noiseMatrix[i][j] < layersElevation[e]) {
                            color = Color.decode(layersColor[e]);
                        }
                    } else if (e < 7){
                        if (noiseMatrix[i][j] > layersElevation[e - 1] && noiseMatrix[i][j] <= layersElevation[e]) {
                            color = Color.decode(layersColor[e]);
                        }
                    }
                    image.setRGB(j, i, color.getRGB());
                }
            }
        }
        MapSaver saver = new MapSaver();
        saver.saveMap(image, "temp/map.png");
    }

    public void saveMap(String url){
        MapSaver saver = new MapSaver();
        saver.saveMap(image, url);
    }
}
