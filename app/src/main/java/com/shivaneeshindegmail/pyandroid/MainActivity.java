package com.shivaneeshindegmail.pyandroid;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.app.Activity;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import com.shivaneeshindegmail.pyandroid.ShellExecuter;

public class MainActivity extends Activity {

    EditText input;
    Button btn;
    TextView out;
    String command,command1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        input = (EditText)findViewById(R.id.txt);
        btn = (Button)findViewById(R.id.btn);
        out = (TextView)findViewById(R.id.out);
        btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {
                // TODO Auto-generated method stub
                ShellExecuter exe = new ShellExecuter();
                command1 = input.getText().toString();
                command="python try.py";
                //command=command.concat(command1);
                String outp = exe.Executer(command);
                out.setText(outp);
                Log.d("Output", outp);
            }
        });

    }

}