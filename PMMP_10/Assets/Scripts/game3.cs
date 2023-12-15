using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game3 : MonoBehaviour
{

    public float speed = 5f;

    void Update()
    {
        // Получаем входные данные для движения
        float horizontalInput = Input.GetAxis("Vertical");
        float verticalInput = -Input.GetAxis("Horizontal");

        transform.rotation = Quaternion.identity; // Устанавливает начальный поворот в единичное положение


        // Вычисляем направление движения
        Vector3 movement = new Vector3(horizontalInput, 0f, verticalInput).normalized;

        // Применяем движение к объекту
        transform.Translate(movement * speed * Time.deltaTime);
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Wall(Clone)")
        {
            Destroy(collision.gameObject);
        }
        else if (collision.gameObject.name == "Cube")
        {
            Destroy(gameObject);
            print("You LOSER!!");
        }
    }
}
