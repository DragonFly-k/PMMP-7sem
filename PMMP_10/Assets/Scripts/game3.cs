using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game3 : MonoBehaviour
{

    public float speed = 5f;

    void Update()
    {
        // �������� ������� ������ ��� ��������
        float horizontalInput = Input.GetAxis("Vertical");
        float verticalInput = -Input.GetAxis("Horizontal");

        transform.rotation = Quaternion.identity; // ������������� ��������� ������� � ��������� ���������


        // ��������� ����������� ��������
        Vector3 movement = new Vector3(horizontalInput, 0f, verticalInput).normalized;

        // ��������� �������� � �������
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
