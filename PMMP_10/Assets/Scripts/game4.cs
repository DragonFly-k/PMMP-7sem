using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game4 : MonoBehaviour
{
    public string nameToDestroy = "Cube";

    void OnTriggerEnter(Collider other)
    {
        // Проверяем, что объект, вошедший в триггер, является сферой
        if (other.gameObject.name == "Sphere")
        {
            // Находим все объекты с указанным тегом и уничтожаем их
            GameObject[] objectsToDestroy = GameObject.FindGameObjectsWithTag(nameToDestroy);
            foreach (GameObject obj in objectsToDestroy)
            {
                Destroy(obj);
            }
        print("You WIN!!");
        }

    }
}