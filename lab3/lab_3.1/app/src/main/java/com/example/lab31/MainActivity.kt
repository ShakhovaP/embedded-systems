package com.example.lab31

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
//import java.lang.Math.sqrt
import kotlin.math.*

class MainActivity : AppCompatActivity() {

//    public final var resultTextView : TextView
    private fun isSquare(n: Double) :Boolean{
    var result = (n === ceil(sqrt(n)).pow(2))
    return result
}

    private fun ferma_factorisation(n: Double) :String{
        val startTime = System.currentTimeMillis()
        var p = 0
        var q = 0
        var result: String
        while(System.currentTimeMillis() !== startTime + 20) {
            var a = ceil(sqrt(n))
            while (!isSquare(a.pow(2) - n)){
                a += 1
            }
            var b = sqrt(a.pow(2) - n)

            p = (a + b).toInt()
            q = (a - b).toInt()
        }
        if (n.toInt() == p*q) {
            result =  "${n.toInt()} = ${p} * ${q}"
        } else {
            result = "Sorry, time is up!"
        }
        return result
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var result: TextView = findViewById(R.id.show_result)
        var inputData: EditText = findViewById(R.id.input_data)

        var buttonCalculate: Button = findViewById(R.id.button_calculate)
        buttonCalculate.setOnClickListener {
            if (inputData.text.isEmpty()){
                result.text = "There was no number entered!"
            } else {
                var test:Double = inputData.text.toString().toDouble()
                result.text = ferma_factorisation(test)
            }
        }
    }
}
