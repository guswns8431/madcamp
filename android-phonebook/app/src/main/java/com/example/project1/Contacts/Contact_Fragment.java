package com.example.project1.Contacts;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;
import java.util.List;

import com.example.project1.IOcustom;
import com.example.project1.MyApplication;
import com.example.project1.R;

import static com.example.project1.MyApplication.getAppContext;

public class Contact_Fragment extends Fragment {


    MyApplication app;

    private RecyclerView mRecyclerView;
    private ContactAdapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;
    private List<Contact> contacts = new ArrayList<>();

    public List<Contact> getContacts(){
        return contacts;
    }

    public Contact_Fragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        app = (MyApplication) getAppContext();
        IOcustom iocustom = new IOcustom();

        super.onCreate(savedInstanceState);

        //List 를 JSON 으로 저장
        //Context context = getContext();
        //String json = new Gson().toJson(contacts);
        //writeToFile(json,getContext());
        contacts = app.getContacts();
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_contacts, container, false);

        mRecyclerView = (RecyclerView)view.findViewById(R.id.contactRV);
        mLayoutManager = new LinearLayoutManager(this.getActivity());
        mRecyclerView.setLayoutManager(mLayoutManager);
        mAdapter = new ContactAdapter(contacts);
        mRecyclerView.setAdapter(mAdapter);

        return view;
    }
}
