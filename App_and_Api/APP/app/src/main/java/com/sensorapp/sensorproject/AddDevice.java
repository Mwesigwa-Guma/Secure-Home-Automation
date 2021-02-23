package com.sensorapp.sensorproject;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;

public class AddDevice extends AppCompatActivity {

    EditText editText;
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_device);


        editText = findViewById(R.id.editText);
        button = findViewById(R.id.button);


        button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                if ( editText.getText().toString().isEmpty()) {
                    Toast.makeText(getApplicationContext(), "Enter device name", Toast.LENGTH_SHORT).show();
                } else {
                    postData("http://10.0.0.146:8888/post.php");
                    //finish();
                    Intent intent = new Intent(AddDevice.this, MainActivity.class);
                    startActivity(intent);
                }
            }
        });

    }

    private void postData(final String urlWebService) {

        class PostData extends AsyncTask<Void, Void, String> {

            @Override
            protected void onPreExecute() {
                super.onPreExecute();
            }

            @Override
            protected void onPostExecute(String s) {
                super.onPostExecute(s);
            }

            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            protected String doInBackground(Void... voids) {
                try {

                    String device_name = editText.getText().toString();
                    String data  = URLEncoder.encode("device_name", "UTF-8") + "=" +
                            URLEncoder.encode(device_name, "UTF-8");


                    URL url = new URL(urlWebService);
                    URLConnection con = url.openConnection();

                    con.setDoOutput(true);
                    //con.setRequestMethod("POST");
                    OutputStreamWriter wr = new OutputStreamWriter(con.getOutputStream());

                    wr.write( data );
                    wr.flush();

                    BufferedReader reader = new BufferedReader(new
                            InputStreamReader(con.getInputStream()));

                    StringBuilder sb = new StringBuilder();
                    String line = null;

                    // Read Server Response
                    while((line = reader.readLine()) != null) {
                        sb.append(line);
                        break;
                    }

                    return sb.toString();
                } catch (Exception e) {
                    Log.e("MyTag", "Error", e);
                    return null;
                }
            }

        }

        PostData pd = new PostData();
        pd.execute();

    }
}