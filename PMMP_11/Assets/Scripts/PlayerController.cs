using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 5f;
    public float raycastRange = 10f;

    private GenerateScillet enemyGenerator;

    void Start()
    {
        enemyGenerator = FindObjectOfType<GenerateScillet>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Shoot();
        }
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(horizontalInput, 0f, verticalInput) * speed * Time.deltaTime;

        transform.Translate(movement);
    }

    void Shoot()
    {
        Vector3 rayStartPosition = transform.position + new Vector3(0f, 1f, 0f);
        Ray ray = new Ray(rayStartPosition, transform.forward);
        RaycastHit hit;
        Debug.DrawRay(ray.origin, ray.direction * raycastRange, Color.red, 4f);

        if (Physics.Raycast(ray, out hit, raycastRange) && hit.collider.CompareTag("Enemy"))
        {
            enemyGenerator.DestroyEnemy(hit.collider.gameObject);

        }
    }
}
