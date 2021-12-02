package com.jd.test;

import org.junit.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class ProblemSolve {
    private Integer plateau_x,plateau_y;
    private ArrayList<Integer> init_x,init_y;
    private ArrayList<String> init_turn,steps;
    private String path;

    public static void main(String[] args) throws IOException {
        ProblemSolve s=new ProblemSolve();
        s.test1();
    }

    public void getInput() throws IOException {
        String origin_path = this.getClass().getProtectionDomain().getCodeSource().getLocation().getPath();
        String[] split = origin_path.split("/");
        path="";
        for (int i = 1; i < split.length-1; i++) {
            path+=split[i]+"/";
        }
        File file = new File(path+"input.txt");
        BufferedReader br=new BufferedReader(new FileReader(file));
        String line;
        init_x=new ArrayList<Integer>();
        init_y=new ArrayList<Integer>();
        init_turn=new ArrayList<String>();
        steps=new ArrayList<String>();
        int cnt=0;
        while ((line=br.readLine())!=null){
            System.out.println(line);
            String[] words=line.split(" ");
            if(cnt==0){
                plateau_x=Integer.parseInt(words[0]);
                plateau_y=Integer.parseInt(words[1]);
            }else
            if((cnt&1)==0){
                steps.add(words[0]);
            }else{
                init_x.add(Integer.parseInt(words[0]));
                init_y.add(Integer.parseInt(words[1]));
                init_turn.add(words[2]);
            }
            cnt+=1;
        }
        br.close();
    }

    public void printOutput(String resString) throws FileNotFoundException {
        PrintWriter output = new PrintWriter(new File(path+"output.txt"));
        output.print(resString);
        output.close();
    }

    @Test
    public void test1() throws IOException {
        getInput();
        // E东 S南 W西 N北
        HashMap<String,String> turnRightTo=new HashMap<>();
        turnRightTo.put("E","S");
        turnRightTo.put("S","W");
        turnRightTo.put("W","N");
        turnRightTo.put("N","E");
        HashMap<String,String> turnLeftTo=new HashMap<>();
        turnLeftTo.put("N","W");
        turnLeftTo.put("W","S");
        turnLeftTo.put("S","E");
        turnLeftTo.put("E","N");
        int res_x,res_y;
        String res_turn,step,resString="";
        for (int i = 0; i < init_x.size(); i++) {
            res_x=init_x.get(i);
            res_y=init_y.get(i);
            res_turn=init_turn.get(i);
            step=steps.get(i);
            for (int j = 0; j < step.length(); j++) {
                if(step.charAt(j)=='L'){
                    res_turn=turnLeftTo.get(res_turn);
                }else
                if(step.charAt(j)=='R'){
                    res_turn=turnRightTo.get(res_turn);
                }
                else{
                    if(res_turn=="N"){
                        res_y+=1;
                    }else
                    if(res_turn=="W"){
                        res_x-=1;
                    }else
                    if(res_turn=="S"){
                        res_y-=1;
                    }else{
                        res_x+=1;
                    }
                }
            }
            resString+=res_x+" "+res_y+" "+res_turn+"\n";
        }
        printOutput(resString);
    }
}
