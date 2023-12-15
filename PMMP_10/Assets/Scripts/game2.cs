using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game2 : MonoBehaviour
{
    private Rigidbody rb;
    public float speed;


    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.velocity = transform.forward * speed; 
    }


    void OnCollisionEnter(Collision collision)
    {
        // Если произошло столкновение
        if (collision.gameObject.name=="Wall" || collision.gameObject.name == "Wall(Clone)")
        {
            Vector3 currentDirection = rb.velocity.normalized;

            // Изменяем направление на противоположное
            Vector3 newDirection = new Vector3(currentDirection.x, currentDirection.y, -currentDirection.z);

            // Применяем новое направление движения
            rb.velocity = newDirection * speed;
        }
    }

}
