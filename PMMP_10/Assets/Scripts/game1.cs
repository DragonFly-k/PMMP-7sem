using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class game1 : MonoBehaviour
{
    public GameObject prefab;

    void Start()
    {
        for (int i = 0; i < 15; i++)
        {
            Vector3 position = new Vector3(Random.Range(-9.0f, 20.0f), 2, Random.Range(-10.0f, 20.0f));
            Instantiate(prefab, position, Quaternion.identity);
        }
    }
}
