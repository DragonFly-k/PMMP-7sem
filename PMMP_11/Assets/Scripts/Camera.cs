using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera : MonoBehaviour
{
    public Transform target;
    public float smoothSpeed = 0.125f; 

    void LateUpdate()
    {
        if (target != null)
        {
            transform.position = new Vector3(Mathf.Lerp(transform.position.x, target.transform.position.x, smoothSpeed), transform.position.y, transform.position.z);


            transform.LookAt(target);
        }
    }
}