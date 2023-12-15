using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game4 : MonoBehaviour
{
    public string nameToDestroy = "Cube";

    void OnTriggerEnter(Collider other)
    {
        // ���������, ��� ������, �������� � �������, �������� ������
        if (other.gameObject.name == "Sphere")
        {
            // ������� ��� ������� � ��������� ����� � ���������� ��
            GameObject[] objectsToDestroy = GameObject.FindGameObjectsWithTag(nameToDestroy);
            foreach (GameObject obj in objectsToDestroy)
            {
                Destroy(obj);
            }
        print("You WIN!!");
        }

    }
}