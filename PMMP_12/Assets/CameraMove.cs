using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMove : MonoBehaviour
{
    public Transform playerBody;
    public float mouseSensivity = 100f;
    float xRotation = 0f;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        float mousex = Input.GetAxis("Mouse X")* mouseSensivity* Time.deltaTime;
        float mousey = Input.GetAxis("Mouse Y") * mouseSensivity * Time.deltaTime;

        xRotation -= mousey;
        xRotation =Mathf.Clamp(xRotation, -90f, 90f);  
        transform.localRotation = Quaternion.Euler(xRotation, 0f,0f);
        playerBody.Rotate(Vector3.up * mousex);
    }
}
