using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ExampleClass : MonoBehaviour
{
    public GameObject prefab;
    
    void Start()
    {
        for (int i = 0; i < 15; i++)
        {
            Vector3 position = new Vector3(Random.Range(-10.0f, 10.0f), Random.Range(0.0f, 10.0f), Random.Range(-10.0f, 10.0f));
        Instantiate(prefab, position, Quaternion.identity);
        }
    }
}
