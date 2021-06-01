package ptg.generators;

import ptg.opensimplex.OpenSimplex2S;

public class Generator {
    private OpenSimplex2S simplex;
    private final int width;
    private final int heidth;
    private double freq;
    private int octaves;

    public Generator(int width, int heidth){
        simplex = new OpenSimplex2S(1);
        this.width = width;
        this.heidth = heidth;
    }

    public void setFreq(double freq) throws Exception {
        if (freq > 0)
            this.freq = freq;
        else
            throw new Exception("Frequência deve ser não negativa!");
    }

    public void setSeed(long seed){
        simplex = new OpenSimplex2S(seed);
    }

    public void setOctaves(int octaves) throws Exception{
        if(octaves > 0 && octaves <= 7)
            this.octaves = octaves;
        else
            throw new Exception("Núemero de oitavas incompatível.\nMínimo: 1\nMáximo: 7");
    }

    private double noise(double nx, double ny){
        return simplex.noise2(freq * nx, freq * ny) / 2.0 + 0.5;
    }

    public double[][] getNoiseMatrix(){
        double nx;
        double ny;
        double[][] noiseMatrix = new double[heidth][width];
        double res = 0;
        double div = 0;
        double dist = 0;
        double cx = (double)width / 2 / (double)width - 0.5;
        double cy = (double)heidth / 2 / (double)heidth - 0.5;

        for(int i = 0; i < heidth; i++){
            for(int j = 0; j < width; j++){
                nx = (double)j / width - 0.5;
                ny = (double)i / heidth - 0.5;

                dist = Math.sqrt(Math.pow(nx - cx, 2) + Math.pow(ny - cy, 2));
                dist = Math.pow(dist, 0.7);

                for(int o = 1; o <= Math.pow(2, octaves - 1); o *= 2){
                    res += (double)1 / o * noise(o * nx, o * ny);
                    div += (double)1 / o;
                }

                res = res / div;
                noiseMatrix[i][j] = (1 + res - dist) / 2;
                res = 0;
                div = 0;
            }
        }
        return noiseMatrix;
    }
}
